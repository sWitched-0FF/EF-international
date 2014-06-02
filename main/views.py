#coding: utf-8
from django.contrib.auth import get_user_model
User = get_user_model()

from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from conversejs.models import XMPPAccount

from gallery.models import ImageGallery, VideoGallery, DocsGallery

from .models import Ad, Calendar, Contest, News, Vacation


class ContextMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(ContextMixin, self).get_context_data(**kwargs)
        try:
            xmpp_account = XMPPAccount.objects.get(user=self.request.user.pk)
            ctx['user_jid'] = xmpp_account
        except XMPPAccount.DoesNotExist: pass
        if Contest.objects.all().exists():
            ctx['contest'] = Contest.objects.all().latest('pk')
        #if Ad.objects.all().exists():
            #ctx['ad'] = Ad.objects.all().latest('pk')
        ctx['ads'] = Ad.objects.all()
        ctx['news'] = News.objects.all()
        ctx['calendar_events'] = Calendar.objects.all()
        ctx['clrs'] = ('blue','green','orange')
        return ctx


class IndexPage(ContextMixin, TemplateView):
    u''' Главная страница '''
    template_name = 'index.html'
index = IndexPage.as_view()
calendar = IndexPage.as_view(template_name='calendar.html')

class ListPage(ContextMixin, ListView):
    model = News
    paginate_by = 10
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        ctx = super(ListPage, self).get_context_data(**kwargs)
        ctx['title'] = self.model._meta.verbose_name_plural
        return ctx    
news_list = ListPage.as_view()
ads_list = ListPage.as_view(model=Ad)
contests_list = ListPage.as_view(model=Contest)


class CompanyLifePage(IndexPage):
    u''' Жизнь компании '''
    template_name = 'company_life.html'

    def get_context_data(self, **kwargs):
        ctx = super(CompanyLifePage, self).get_context_data(**kwargs)
        ctx['contests'] = Contest.objects.all()
        ctx['image_galleries'] = ImageGallery.objects.all()
        ctx['video_galleries'] = VideoGallery.objects.all()
        return ctx
company_life = CompanyLifePage.as_view()


class InfoPage(IndexPage):
    u''' Справочная информация '''
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        ctx = super(self.__class__, self).get_context_data(**kwargs)
        ctx['phones_info'] = User.objects.with_phones()
        ctx['docs_galleries'] = DocsGallery.objects.all()
        ctx['video_galleries'] = VideoGallery.objects.all()
        return ctx
info = InfoPage.as_view()


class StaffPage(IndexPage):
    u''' Сотрудники '''
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        ctx = super(StaffPage, self).get_context_data(**kwargs)
        ctx['birthday_users'] = User.objects.birthday_users()
        ctx['new_users'] = User.objects.new_users()
        ctx['on_vacations'] = Vacation.objects.on_vacation_users()
        return ctx
staff = StaffPage.as_view()


class DetailPage(ContextMixin, DetailView):
    template_name = 'object_detail.html'
    context_object_name = 'detail_page'

    def get_context_data(self, **kwargs):
        ctx = super(DetailPage, self).get_context_data(**kwargs)
        ctx['reverse_url_name'] = ctx.get('detail_page'
                                    ).__class__._meta.verbose_name_plural.lower()
        return ctx

ads = DetailPage.as_view(model=Ad)
calendar_event = DetailPage.as_view(model=Calendar)
contests = DetailPage.as_view(model=Contest)
news = DetailPage.as_view(model=News)