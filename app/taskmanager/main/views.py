from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Symptoms, Questions, Diseases


class MainView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'main/base.html', context=self.get_context())

    def get_context(self):
        context = {}
        context['title'] = "Главная"
        return context


class DiseasesListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'main/diseases.html', context=self.get_context())

    def get_context(self):
        context = {}
        context['diseases'] = Diseases.objects.all().order_by('title')
        context['category_name'] = 'Болезни'
        return context


class SymptomsListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'main/symptoms.html', context=self.get_context())

    def get_context(self):
        context = {}
        context['symptoms'] = Symptoms.objects.all().order_by('title')
        context['category_name'] = 'Симптомы'
        return context


class DiseaseDetailView(View):
    def get(self, *args, **kwargs):
        disease = Diseases.objects.filter(id=kwargs.get('disease_id')).first()
        if not disease:
            return HttpResponse('''
                        <h1>Страница не найдена</h1>
                    ''')

        context = {"disease": disease, 'symptoms': disease.symptoms.all(), 'causes': disease.causes.all()}
        return render(self.request, 'main/disease_detail.html', context=context)


class SymptomDetailView(View):
    def get(self, *args, **kwargs):
        symptom = Symptoms.objects.filter(id=kwargs.get('symptom_id')).first()
        if not symptom:
            return HttpResponse('''
                        <h1>Страница не найдена</h1>
                    ''')

        context = {"symptom": symptom, 'diseases': symptom.diseases.all()}
        return render(self.request, 'main/symptom_detail.html', context=context)


class QuestionView(View):
    def post(self, *args, **kwargs):
        Questions.objects.create(
            title=self.request.POST.get('title'),
            question=self.request.POST.get('question'),
            email=self.request.POST.get('email'),
        )
        return HttpResponseRedirect('/')
