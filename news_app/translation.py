from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from news_app.models import News, Category


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', )

@register(Category)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )