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

ads_list = IndexPage.as_view(template_name='news_list.html')
index = IndexPage.as_view()
info = IndexPage.as_view(template_name = 'info.html')
news_list = IndexPage.as_view(template_name = 'news_list.html')
calendar = IndexPage.as_view(template_name='calendar.html')
contests_list = IndexPage.as_view(template_name='news_list.html')


class CompanyLifePage(IndexPage):
    u''' Жизнь компании '''
    template_name = 'company_life.html'

    def get_context_data(self, **kwargs):
        ctx = super(CompanyLifePage, self).get_context_data(**kwargs)
        ctx['contests'] = Contest.objects.all()
        return ctx
company_life = CompanyLifePage.as_view()


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

ads = DetailPage.as_view(model=Ad)
calendar_event = DetailPage.as_view(model=Calendar)
contests = DetailPage.as_view(model=Contest)
news = DetailPage.as_view(model=News)