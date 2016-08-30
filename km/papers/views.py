from django.shortcuts import render
from django.utils import timezone
from .models import Paper
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchPapers
from django.db.models import Q
from collections import Counter
import operator
import json

sourceFullName = {'MISQ': 'MIS QUARTERLY', 
			      'ISR': 'INFORMATION SYSTEMS RESEARCH',
				  'JMIS': 'JOURNAL OF MANAGEMENT INFORMATION SYSTEMS',
				  'JAIS': 'JOURNAL OF THE ASSOCIATION FOR INFORMATION SYSTEMS',
				  'JSIS': 'JOURNAL OF STRATEGIC INFORMATION SYSTEMS',
				  'ISJ': 'INFORMATION SYSTEMS JOURNAL',
				  'JIT': 'JOURNAL OF INFORMATION TECHNOLOGY',
				  'EJIS': 'EUROPEAN JOURNAL OF INFORMATION SYSTEMS'}				  
				  
def paper_list(request):
	results= Paper.objects.filter(id=199)
	form = SearchPapers(initial={'MISQ': 1,'ISR':1})
	return render(request, 'papers/paper_list.html', {'papers': results,'form': form})

		
	#return render(request, 'papers/paper_list.html', {'papers': results, 'query': q})
	

def search(request):
	subSample=Paper.objects.none()
	for s in ['MISQ', 'ISR', 'JMIS','JAIS','JSIS','ISJ','JIT','EJIS']:
		if s in request.GET:
			subSample=subSample|Paper.objects.filter(source=sourceFullName[s])
	q = request.GET['title_search']
	author=request.GET['author_search']
	results = subSample.filter(Q(title__icontains=q)| Q(keywords__icontains=q) ,authors__icontains=author)
	form = SearchPapers(request.GET)
	return render(request, 'papers/paper_list.html', {'papers': results,'form': form})	
	#return render(request, 'papers\paper_list.html',{'papers': papers, 'query': q})


def title(request):
	if 'id' in request.GET and request.GET['id']:
		tab = request.GET['tab']
		id = request.GET['id']
		papers = Paper.objects.filter(id=id)
		form = SearchPapers(request.GET)
		
		#similar articles
		sims=papers[0].sim.split(',')
		sims=[sim.strip('[( )]') for sim in sims]
		it=iter(sims)
		sims=zip(it,it)
		sim_scores=[sim[1] for sim in sims]
		sim_papers=[]
		for sim in sims[0:10]:
			sim_papers.append(Paper.objects.filter(index=sim[0])[0])
		papers_sims=zip(sim_papers,sim_scores)
		
		#reference articles
		ref_papers=[]
		if (papers[0].refs!='[]'):
			refs=papers[0].refs.split(',')
			refs=[ref.strip('[ ]') for ref in refs]
			for ref in refs:
				ref_papers.append(Paper.objects.filter(index=ref)[0])
	return render(request, 'papers/paper_list.html',
		{'papers': papers, 'id': id, 'form': form, 'papers_sims' : papers_sims, 'ref_papers':ref_papers, 'tab':tab})
		
def author(request):
	author = request.GET['author'].strip()
	papers = Paper.objects.filter(authors__icontains=author)
	coauthors=[]
	for paper in papers:
		coauthors=coauthors+paper.authors.split(';')
		coauthors=[co.strip() for co in coauthors]
	coauthors=[x for x in coauthors if x.lower() != author.lower()]
	list_tuple=Counter(coauthors).most_common()
	coauthors_unique=[list(elem) for elem in list_tuple]
	form = SearchPapers(request.GET)
	return render(request, 'papers/paper_list.html',
		{'papers': papers, 'author': author, 'coauthors_unique': coauthors_unique, 'form': form})

def keyword(request):
	keyword = request.GET['keyword'].strip()
	papers = Paper.objects.filter(keywords__icontains=keyword)
	cokeywords=[]
	for paper in papers:
		cokeywords=cokeywords+paper.keywords.split(';')
		cokeywords=[co.strip() for co in cokeywords]
	cokeywords=[x for x in cokeywords if x.lower() != keyword.lower()]
	list_tuple=Counter(cokeywords).most_common()
	cokeywords_unique=[list(elem) for elem in list_tuple]
	form = SearchPapers(request.GET)
	return render(request, 'papers/paper_list.html',
		{'papers': papers, 'keyword': keyword, 'cokeywords_unique':cokeywords_unique,'form': form})
