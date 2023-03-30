from django.shortcuts import render
def 성훈(request):
    context = {
        'name': '문성훈',
        'imgUrl': 'https://i.namu.wiki/i/4mvF8blu1mgV_R8yWpKKV7lEis6Vz7tvXVp5zQ7OPMebhZUZsyM_lhlHxhuml8VQsZqoqhtqXD9pjjmw_JBHCcQ3cp0qQ0D8fhziELQA0adoIEWPS55TaJoz-fmKfseobfjjXlxzcojKA4XV2Q_J2w.webp',
    }
    return render(request, "NRG/성훈.html", context=context)

def 명훈(request):
    context = {
        'name': '천명훈',
        'imgUrl': 'https://www.dailysecu.com/news/photo/202001/92687_100149_4733.png',
    }
    return render(request, "NRG/명훈.html", context=context)
# Create your views here.
