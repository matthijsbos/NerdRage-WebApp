# import asyncio
# from os import environ
# import datetime

from autobahn.asyncio.wamp import ApplicationSession, ApplicationSessionFactory
# from autobahn.wamp.exception import ApplicationError
from autobahn.asyncio.component import Component, run

class MyApplication:
    
    poslim = True
    session: ApplicationSession
    session = None
   
#     def create_session(self, config=None):
#         return MySession(self, config=config)



# class MySession(ApplicationSession):

#     def __init__(self, app: MyApplication, config=None):
#         super().__init__(config)
#         self.app = app
            

    # async def onJoin(self, details):

        

    #     print('connected')

    #     def set_poslim(poslim):
    #         self.poslim = poslim

    #     def get_poslim():
    #         return self.poslim

    #     await self.register(get_poslim, 'nl.matthijsbos.nerdrage.get_poslim')
    #     await self.register(set_poslim, 'nl.matthijsbos.nerdrage.set_poslim')

    #     print('registered')



if __name__ == '__main__':
    app = MyApplication()

    print('mock controller')
    
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')


    @comp.on_join
    def joined(session, details):
        print("session joined")
        app.session = session

    @comp.register('nl.matthijsbos.nerdrage.set_poslim')
    def set_poslim(poslim):
        print('set_poslim', poslim)
        app.poslim = poslim
        if poslim:
            print("publish poslim activated")
            app.session.publish('nl.matthijsbos.nerdrage_poslim_activated')
        else:
            print("publish poslim deactivated")
            app.session.publish('nl.matthijsbos.nerdrage_poslim_deactivated')

    @comp.register('nl.matthijsbos.nerdrage.get_poslim')
    def get_poslim():
        print('get_poslim', app.poslim)
        return app.poslim

    run([comp])