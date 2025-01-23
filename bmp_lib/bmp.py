def summaries_and_audio(text):
    abstractif = text[:20]
    extractif = text[20:100]
    audio = None
    return abstractif, extractif, audio



class Summary:
    def __init__(self, content):
        self.content = content
        self.audio_file = None

    def get_summary_content(self):
        return self.content
    
    def get_summary_audio_file(self):
        return self.audio_file



class ExtractiveSummary(Summary):
    def __init__(self, content):
        super().__init__(content)


class AbstractiveSummary(Summary):
    def __init__(self, content):
        super().__init__(content)




class ArticleItem:
    def __init__(self, name):
        self.content = None
        self.abstractiveSummary = None
        self.extractiveSummary = None

    def get_abstractiveSummary(self):
        return self.abstractiveSummary
    
    def get_abstractiveSummary(self):
        return self.extractiveSummary
    
    def get_article_content(self):
        return self.content
    


class MediaStore:
    def __init__(self, name):
        self.name = None
        self.articles = []

    def get_media_name(self):
        return self.name
    
    def get_articles(self):
        return self.articles
    
    def count_article(self):
        return len(self.articles)
