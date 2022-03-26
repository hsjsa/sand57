from bot.helper.telegram_helper.message_utils import sendMessage
from bot import AUTHORIZED_CHATS, SUDO_USERS, dispatcher, DB_URI
from telegram.ext import CommandHandler
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.db_handler import DbManger


def authorize(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in AUTHORIZED_CHATS:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ☻'
        elif DB_URI is not None:
            msg = DbManger().db_auth(user_id)
        else:
            with open('authorized_chats.txt', 'a') as file:
                file.write(f'{user_id}\n')
                AUTHORIZED_CHATS.add(user_id)
                msg = '𝐔𝐬𝐞𝐫 𝐀𝐮𝐭𝐡𝐫𝐨𝐫𝐢𝐳𝐞𝐝 ✔️\n\n <b>Now He Can use Bot In PM</b>'
    elif reply_message is None:
        # Trying to authorize a chat
        chat_id = update.effective_chat.id
        if chat_id in AUTHORIZED_CHATS:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐂𝐡𝐚𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝.☻'

        elif DB_URI is not None:
            msg = DbManger().db_auth(chat_id)
        else:
            with open('authorized_chats.txt', 'a') as file:
                file.write(f'{chat_id}\n')
                AUTHORIZED_CHATS.add(chat_id)
                msg = '𝐂𝐡𝐚𝐭 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ✔️\n\n<b>Now Chat Members Can Use Bot</b>'
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in AUTHORIZED_CHATS:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ☻'
        elif DB_URI is not None:
            msg = DbManger().db_auth(user_id)
        else:
            with open('authorized_chats.txt', 'a') as file:
                file.write(f'{user_id}\n')
                AUTHORIZED_CHATS.add(user_id)
                msg = '𝐔𝐬𝐞𝐫 𝐀𝐮𝐭𝐡𝐫𝐨𝐫𝐢𝐳𝐞𝐝 ✔️\n\n <b>Now He Can use Bot In PM</b>'
    sendMessage(msg, context.bot, update)


def unauthorize(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().db_unauth(user_id)
            else:
                AUTHORIZED_CHATS.remove(user_id)
                msg = '𝐔𝐬𝐞𝐫 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 \n\n<b>Bye Bye To Him</b>'
        else:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝'
    elif reply_message is None:
        # Trying to unauthorize a chat
        chat_id = update.effective_chat.id
        if chat_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().db_unauth(chat_id)
            else:
                AUTHORIZED_CHATS.remove(chat_id)
                msg = '𝐂𝐡𝐚𝐭 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ⍢ \n\n<b>Kthnxbye Memebrs</b>'
        else:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐂𝐡𝐚𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 ☻'
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in AUTHORIZED_CHATS:
            if DB_URI is not None:
                msg = DbManger().db_unauth(user_id)
            else:
                AUTHORIZED_CHATS.remove(user_id)
                msg = '𝐔𝐬𝐞𝐫 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 \n\n<b>Bye Bye To Him</b>'
        else:
            msg = '𝐍𝐨 𝐍𝐞𝐞𝐝!! 𝐔𝐬𝐞𝐫 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝'
    with open('authorized_chats.txt', 'a') as file:
        file.truncate(0)
        for i in AUTHORIZED_CHATS:
            file.write(f'{i}\n')
    sendMessage(msg, context.bot, update)


def addSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            msg = 'Already Sudo'
        elif DB_URI is not None:
            msg = DbManger().db_addsudo(user_id)
        else:
            with open('sudo_users.txt', 'a') as file:
                file.write(f'{user_id}\n')
                SUDO_USERS.add(user_id)
                msg = 'Promoted as Sudo'
    elif reply_message is None:
        msg = "Give ID or Reply To message of whom you want to Promote"
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            msg = 'Already Sudo'
        elif DB_URI is not None:
            msg = DbManger().db_addsudo(user_id)
        else:
            with open('sudo_users.txt', 'a') as file:
                file.write(f'{user_id}\n')
                SUDO_USERS.add(user_id)
                msg = 'Promoted as Sudo'
    sendMessage(msg, context.bot, update)


def removeSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            if DB_URI is not None:
                msg = DbManger().db_rmsudo(user_id)
            else:
                SUDO_USERS.remove(user_id)
                msg = 'Demoted'
        else:
            msg = 'Not a Sudo'
    elif reply_message is None:
        msg = "Give ID or Reply To message of whom you want to remove from Sudo"
    else:
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            if DB_URI is not None:
                msg = DbManger().db_rmsudo(user_id)
            else:
                SUDO_USERS.remove(user_id)
                msg = 'Demoted'
        else:
            msg = 'Not a Sudo'
    if DB_URI is None:
        with open('sudo_users.txt', 'a') as file:
            file.truncate(0)
            for i in SUDO_USERS:
                file.write(f'{i}\n')
    sendMessage(msg, context.bot, update)


def sendAuthChats(update, context):
    user = sudo = ''
    user += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
    sudo += '\n'.join(str(id) for id in SUDO_USERS)
    sendMessage(f'<b><u>Authorized Chats</u></b>\n<code>{user}</code>\n<b><u>Sudo Users</u></b>\n<code>{sudo}</code>', context.bot, update)


send_auth_handler = CommandHandler(command=BotCommands.AuthorizedUsersCommand, callback=sendAuthChats,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
authorize_handler = CommandHandler(command=BotCommands.AuthorizeCommand, callback=authorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
unauthorize_handler = CommandHandler(command=BotCommands.UnAuthorizeCommand, callback=unauthorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
addsudo_handler = CommandHandler(command=BotCommands.AddSudoCommand, callback=addSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)
removesudo_handler = CommandHandler(command=BotCommands.RmSudoCommand, callback=removeSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)

dispatcher.add_handler(send_auth_handler)
dispatcher.add_handler(authorize_handler)
dispatcher.add_handler(unauthorize_handler)
dispatcher.add_handler(addsudo_handler)
dispatcher.add_handler(removesudo_handler)
