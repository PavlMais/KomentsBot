

class CallbackHandler(object):
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.methods = {
            'main_menu' : view.main_menu,
            'ch_list'   : view.ch_list,
            'add_ch'    : view.add_ch,
            'ch_setting': view.ch_setting
        }

    def main(self, bot, update):
        print(update.callback_query.data)
        
        data = update.callback_query.data
        msg  = update.callback_query.message

        data = data.split()

        if data[0] == 'open':
            if len(data) == 3:# for chanel id arg
                self.methods[data[1]](msg, ch_id = data[2])

            self.methods[data[1]](msg)

        elif data[0] == 'comment':
            if data[1] == 'like':
                self.db.like_comment(data[2])

            elif data[1] == 'dislike':
                self.db.dislike_comment(data[2])

            elif data[1] == 'delete':
                self.db.delete_comment(data[2])


            #TODO: update comments list for user and post for chennel
