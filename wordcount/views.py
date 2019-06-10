from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] #글 자체, 문자
    words = text.split()
    word_dic = {}
    
    for word in words:
        if word in word_dic:
            #increase
            word_dic[word]+=1
        else:
            #add to dictionary
            word_dic[word]=1

    sorted_word_dic = sorted(word_dic.items(), key=(lambda x: x[1]), reverse = True)

    return render(request, 'result.html', {'full':text,'total':len(words),'dictionary':sorted_word_dic})