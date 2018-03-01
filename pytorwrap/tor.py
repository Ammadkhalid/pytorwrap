from stem.control import Controller
from .exception import *

import socket
import socks
import stem
import requests
from time import sleep

class Tor:

    # default socket for removing socks proxy
    socket = socket.socket
    # for checking if the socket is already connected to tor, if yes then disconnect and try
    isSocketConnected = False

    @staticmethod
    def renewConnection(host = '127.0.0.1', port = 9051, password = None):
        """This function is used to ask the controller to change the identity.

        Parameters
        ----------
        host : str
            Tor Host name who have running tor connection.
        port : int
            Tor Host Port.
        password : str
            Authentication Password Used to login in The tor conection of host.

        Returns
        -------
        type:


        """


        # handle tor controller errors
        try:
            controller = Controller.from_port(host, port)
        except stem.SocketError as e:
            errorCode = e.args[0].errno
            if errorCode == 111:
                raise TorNotActive('Tor is not listening on {}:{} '.format(host, port))
            else:
                raise e

        # check for Authentication errors
        try:
            controller.authenticate(password=password)
        except stem.connection.PasswordAuthFailed as e:
            raise InvalidPassword('Cannot able to Authenticate')

        except stem.connection.AuthenticationFailure as exc:
            raise InvalidAuth('Cannot able to Authenticate')

        controller.signal(stem.Signal.NEWNYM)

        # close controller connection
        controller.close()

    def setSocks(self, host, port):
        """Set Socks is used to connect the socket to tor connection.

        Parameters
        ----------
        host : str
            hostname.
        port : int
            port of host.

        Returns
        -------
        type


        """


        # set default proxy to socks 5
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, host, port)
        # set it our socket
        socket.socket = socks.socksocket
        # set it to true
        self.isSocketConnected = True

    def removeSock(self):
        """this is non-staticmethod used to disconnect socket from tor in order to renewIP

        Returns
        -------
        type
            None

        """
        if self.isSocketConnected:
            socket.socket = self.socket

            self.isSocketConnected = False

    @staticmethod
    def verifyIP(old):
        """Verify If the ip has been changed

        Parameters
        ------
        old : str
        IP must be str

        Returns True or False
        -------
        type
            Bool

        """

        # new
        new = requests.get('http://icanhazip.com').text

        return new == old

    def renewIP(self, host = '127.0.0.1', port = 9051, password = None, proxyHost = '127.0.0.1', proxyPort = 9050):
        """The Main function used to renew renew ip (identity) .

        Parameters
        ----------
        host : str
             Default is localhost (127.0.0.1).
        port : int
            Default Port is 9051.
        password : str
            The Authentication Password to gain control to tor connection.

        proxyHost : str
             Default is localhost (127.0.0.1).
        proxyHostport : int
            Default Port is 9050.

        Returns
        -------
        type


        """

        # send request for old ip
        old = requests.get('http://icanhazip.com').text

        # check for socket
        self.removeSock()

        # call renewConnection
        self.renewConnection(host, port, password)
        # now set the socks proxy
        self.setSocks(proxyHost, proxyPort)

        # delay
        delay = 3

        # now check here
        while self.verifyIP(old):
            sleep(delay)
            old = requests.get('http://icanhazip.com').text
