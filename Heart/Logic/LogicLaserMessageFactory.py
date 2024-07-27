from Heart.Packets.Client.ClientHelloMessage import ClientHelloMessage
from Heart.Packets.Client.LoginMessage import LoginMessage
from Heart.Packets.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Heart.Packets.Client.EndClientTurnMessage import EndClientTurnMessage
from Heart.Packets.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Heart.Packets.Client.GoHomeMessage import GoHomeMessage
from Heart.Packets.Client.GetPlayerProfileMessage import GetPlayerProfileMessage
from Heart.Packets.Client.KeepAliveMessage import KeepAliveMessage
from Heart.Packets.Server.LoginFailedMessage import LoginFailedMessage
from Heart.Packets.Server.LoginOkMessage import LoginOkMessage
from Heart.Packets.Server.OutOfSyncMessage import OutOfSyncMessage
from Heart.Packets.Server.ServerHelloMessage import ServerHelloMessage
from Heart.Packets.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Heart.Packets.Server.LobbyInfoMessage import LobbyInfoMessage
from Heart.Packets.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Heart.Packets.Server.KeepAliveServerMessage import KeepAliveServerMessage
from Heart.Packets.Server.PlayerProfileMessage import PlayerProfileMessage



class LogicLaserMessageFactory:
    messagesList = {
        10100: ClientHelloMessage,
        10101: LoginMessage,
        10108: KeepAliveMessage,
        10212: ChangeAvatarNameMessage,
        14101: GoHomeMessage,
        14102: EndClientTurnMessage,
        15081: GetPlayerProfileMessage,
        17750: GoHomeFromOfflinePractiseMessage,
        20100: ServerHelloMessage,
        20103: LoginFailedMessage,
        20104: LoginOkMessage,
        20108: KeepAliveServerMessage,
        23457: LobbyInfoMessage,
        24101: OwnHomeDataMessage,
        24104: OutOfSyncMessage,
        24111: AvailableServerCommandMessage,
        24113: PlayerProfileMessage,
    }

    def getMessageName(messageType):
        try:
            message = LogicLaserMessageFactory.messagesList[messageType]
        except KeyError:
            message = str(messageType)
        if type(message) == str:
            return message
        else:
            return message.__name__

    def messageExist(messageType):
        return (messageType in LogicLaserMessageFactory.messagesList.keys())

    def createMessageByType(messageType, messagePayload):
        messagesList = LogicLaserMessageFactory.messagesList
        if LogicLaserMessageFactory.messageExist(messageType):
            if type(messagesList[messageType]) == str:
                print(LogicLaserMessageFactory.getMessageName(messageType), "skipped")
            else:
                print(LogicLaserMessageFactory.getMessageName(messageType), "created")
                return messagesList[messageType](messagePayload)
        else:
            print(messageType, "skipped")
            return None
