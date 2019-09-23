import cherrypy
import os

MEDIA_DIR = os.path.join(os.path.abspath("."), u"static")

class Myapp(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))


config = {
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': MEDIA_DIR,
        'tools.staticdir.index': "index.html",
    }
}

cherrypy.quickstart(Myapp(), '/', config)