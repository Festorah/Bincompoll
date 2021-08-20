from django.shortcuts import render
from .models import *


def home(request):

	polling_units = PollingUnit.objects.all()
	party_names = Party.objects.all()


	context = {
		'polling_units': polling_units,
		'party_names': party_names,
	}


	return render(request, 'poll/index.html', context)

def pu_result(request):

	announced_polling_unit_result = AnnouncedPollingUnitResult.objects.all()
	polling_units = PollingUnit.objects.all()

	if request.method == 'GET':

		if 'polling_unit_name' in request.GET:
			polling_unit_name = request.GET['polling_unit_name']
			#To be sure its not an empty request
			if polling_unit_name:
				polling_unit = polling_units.filter(polling_unit_name=polling_unit_name)[0]
				polling_unit_uniqueid = polling_unit.unique_id
				results = list(announced_polling_unit_result.filter(polling_unit_uniqueid=polling_unit_uniqueid))
				polling_result_sum  = sum([n.party_score for n in results])

				context = {
					'results': results,
					'polling_result_sum' : polling_result_sum,
					'polling_unit_name': polling_unit_name,
					'polling_units': polling_units,
				}

				return render(request, 'poll/pu_result.html', context)

			else:
				return render(request, 'poll/index.html', context)

	return render(request, 'poll/index.html')



def lga_page(request):

	lgas = Lga.objects.all()

	context = {
		'lgas': lgas,
	}


	return render(request, 'poll/lga_page.html', context)


def lga_result(request):

	polling_unit = PollingUnit.objects.all()
	announced_polling_unit_result = AnnouncedPollingUnitResult.objects.all()
	announced_lga_result = AnnouncedLgaResults.objects.all()

	lgas = Lga.objects.all()
	if request.method == 'GET':

		if 'lga_name' in request.GET:
			lga_name = request.GET['lga_name']
			#To be sure its not an empty request
			if lga_name:
				lga = lgas.get(lga_name=lga_name)
				lga_id = lga.lga_id

				#lga => polling unit => polling unit unique id => announced polling unit uniqueid

				# The intersect between lga and polling unit is the lga_id
				polling_unit_lga_id = list(polling_unit.filter(lga_id=lga_id))

				#Initializing the list to sum up all the party scores in each polling unit
				lga_total_score = []

				#The connector between the polling units and the announced polling unit is the uniqueid
				for unique_id in polling_unit_lga_id:
					unique_id = unique_id.unique_id
					announced_polling_unit_result = list(announced_polling_unit_result.filter(polling_unit_uniqueid=unique_id))


					for score in announced_polling_unit_result:
						party_score = (lga_total_score.append(score.party_score))

					#Returning to a model object for iteration to continue
					announced_polling_unit_result = AnnouncedPollingUnitResult.objects.all()

				#The summation of all the polling units in a lga for each party's party_score
				lga_total_final = sum(lga_total_score)


				#lga announced result
				announced_lga_result = list(announced_lga_result.filter(lga_id=lga_id))

				#Initializing the list to sum up all the party scores in all the lga's
				announced_lga_result_sum = []
				for n in announced_lga_result:
					announced_lga_result_sum.append(n.party_score)

				# announced_lga_result = [sum(n) for n in announced_lga_result]
				announced_lga_result_sum = sum(announced_lga_result_sum)


			context = {
				'lga_total_score': lga_total_final,
				'lga_name': lga_name,
				'announced_lga_result_sum': announced_lga_result_sum,
				'lgas': lgas
				}


			return render(request, 'poll/lga_result.html', context)



def create_pu(request):

	#Unique id must be unique to avoid error
	unique_id = int(str(PollingUnit.objects.order_by('-unique_id')[0])) + 1

	context = {
				'unique_id': unique_id,
				}


	return render(request, 'poll/create_pu.html', context)

def store_apu_result(request):

	parties = Party.objects.all()

	if request.method == 'POST':
		polling_unit = PollingUnit()

		polling_unit.unique_id = request.POST.get('unique_id')
		polling_unit.polling_unit_id = request.POST.get('polling_unit_id')
		polling_unit.ward_id = request.POST.get('ward_id')
		polling_unit.lga_id = request.POST.get('lga_id')
		polling_unit.unique_ward_id = request.POST.get('unique_ward_id')
		polling_unit.polling_unit_number = request.POST.get('polling_unit_number')
		polling_unit.polling_unit_name = request.POST.get('polling_unit_name')
		polling_unit.polling_unit_description = request.POST.get('polling_unit_description')
		polling_unit.save()

		unique_id = int(str(PollingUnit.objects.order_by('-unique_id')[0]))

		context = {
					'unique_id': unique_id,
					'parties': parties,
					}

		return render(request, 'poll/store_apu_result.html',context)


def store_result_apu(request, unique_id):
	#Importing all the necessary models
	party = Party.objects.all()
	announced_polling_unit_result = AnnouncedPollingUnitResult.objects.all()
	result_id = int(str(announced_polling_unit_result.order_by('-result_id')[0]))+1

	#To save each party's result with different party_score, result_id but same unique id(unique id(for announce poling unit) have to be thesame for corresponding polling unit)

	#You can turn this into list comprehension much later... for simplification and logic
	if request.method == 'POST':
		count = 1
		#Iterate through the form and extract data
		for n in party:
			party_name = n.party_name
			data = str(count) + str(party_name)
			count += 1
			party_score = request.POST.get(data)
			announced_polling_unit_result.create(result_id=result_id, 
				polling_unit_uniqueid=unique_id, 
				party_abbreviation=party_name, 
				party_score=party_score
				)
			announced_polling_unit_result.save()
			result_id += 1

	context = {
				'unique_id': unique_id,
				}


	return render(request, 'poll/index.html', context)