#coding: utf-8
from django.contrib.auth import get_user_model
User = get_user_model()

from django.views.generic import DetailView
from django.views.generic import TemplateView

from conversejs.models import XMPPAccount

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
        return ctx


class IndexPage(ContextMixin, TemplateView):
    u''' Главная страница '''
    template_name = 'index.html'
index = IndexPage.as_view()


class CompanyLifePage(ContextMixin, TemplateView):
    u''' Жизнь компании '''
    template_name = 'company_life.html'

    def get_context_data(self, **kwargs):
        ctx = super(CompanyLifePage, self).get_context_data(**kwargs)
        ctx['contests'] = Contest.objects.all()
        return ctx
company_life = CompanyLifePage.as_view()


class InfoPage(ContextMixin, TemplateView):
    u''' Справочная информация '''
    template_name = 'info.html'
info = InfoPage.as_view()


class NewsPage(ContextMixin, TemplateView):
    u''' страница новостей '''
    template_name = 'news_list.html'
news_list = NewsPage.as_view()


class StaffPage(ContextMixin, TemplateView):
    u''' Сотрудники '''
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        ctx = super(StaffPage, self).get_context_data(**kwargs)
        ctx['birthday_users'] = User.objects.birthday_users()
        ctx['new_users'] = User.objects.new_users()
        ctx['on_vacations'] = Vacation.objects.on_vacation_users()
        return ctx
staff = StaffPage.as_view()


class AdsDetailPage(ContextMixin, DetailView):
    u''' Объявление доски объявлений. '''
    template_name = 'ad_detail.html'
    model = Ad
    context_object_name = 'ad_detail'
ads = AdsDetailPage.as_view()


class ContestsDetailPage(ContextMixin, DetailView):
    u''' Объявление доски объявлений. '''
    template_name = 'contest_detail.html'
    model = Contest
    context_object_name = 'contest_detail'
contests = ContestsDetailPage.as_view()


class NewsDetailPage(ContextMixin, DetailView):
    u''' Новость. '''
    template_name = 'news_detail.html'
    model = News
    context_object_name = 'newsdetail'
news = NewsDetailPage.as_view()