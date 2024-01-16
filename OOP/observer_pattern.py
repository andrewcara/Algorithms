from typing import Any


class YoutubeChannel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
        
    def subscribe(self, sub):
        self.subscribers.append(sub)
    
    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)
            
from abc import ABC, abstractmethod

class Youtubesubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass
class YoutubeUser(Youtubesubscriber):
    def __init__(self,name) -> None:
        self.name = name
    
    def sendNotification(self, channel, event):
        print(self.name, channel, event)
        
channel = YoutubeChannel("andrew")

channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))

channel.notify("A new release")