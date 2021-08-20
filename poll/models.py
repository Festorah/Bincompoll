from django.db import models

class PollingUnit(models.Model):

	unique_id = models.IntegerField(("unique_id"))
	polling_unit_id = models.IntegerField(("polling_unit_id")) 
	ward_id = models.IntegerField(("ward_id"))
	lga_id = models.IntegerField(("lga_id"))
	unique_ward_id = models.IntegerField(("unique_ward_id"))
	polling_unit_number = models.CharField(("polling_unit_number"), max_length=200)
	polling_unit_name = models.CharField(("polling_unit_name"), max_length=200)
	polling_unit_description = models.TextField(("polling_unit_description"), default='Polling unit description...', blank=True, null=True)

	def __str__(self):
		return str(self.unique_id)


class AnnouncedLgaResults(models.Model):

	result_id = models.IntegerField(("result_id"))
	lga_id = models.IntegerField(("lga_id")) 
	party_abbreviation = models.CharField(("party_abbreviation"), max_length=200)
	party_score = models.IntegerField(("party_score"))
	entered_by_user = models.CharField(("entered_by_user"), max_length=200)
	date_entered = models.DateTimeField(("date_entered"))

	def __str__(self):
		return str(self.result_id)


class Lga(models.Model):

	unique_id = models.IntegerField(("unique_id"))
	lga_id = models.IntegerField(("lga_id")) 
	lga_name = models.CharField(("lga_name"), max_length=200)
	state_id = models.IntegerField(("state_id"))
	lga_description = models.TextField(("lga_description"), default='LGA description...', blank=True, null=True)

	def __str__(self):
		return str(self.lga_id)


class AnnouncedPollingUnitResult(models.Model):

	result_id = models.IntegerField(("result_id"))
	polling_unit_uniqueid = models.IntegerField(("polling_unit_uniqueid")) 
	party_abbreviation = models.CharField(("party_abbreviation"), max_length=200)
	party_score = models.IntegerField(("party_score"))

	def __str__(self):
		return str(self.result_id)


class AnnouncedStateResult(models.Model):

	result_id = models.IntegerField(("result_id"))
	state_name = models.IntegerField(("state_name")) 
	party_abbreviation = models.CharField(("party_abbreviation"), max_length=200)
	party_score = models.IntegerField(("party_score"))

	def __str__(self):
		return str(self.state_name)


class AnnouncedWardResult(models.Model):

	result_id = models.IntegerField(("result_id"))
	ward_name = models.IntegerField(("ward_name")) 
	party_abbreviation = models.CharField(("party_abbreviation"), max_length=200)
	party_score = models.IntegerField(("party_score"))


	def __str__(self):
		return str(self.ward_name)



class Ward(models.Model):

	unique_id = models.IntegerField(("unique_id"))
	ward_id = models.IntegerField(("ward_id"))
	ward_name = models.CharField(("ward_name"), max_length=200)
	lga_id = models.IntegerField(("lga_id"))
	ward_description = models.TextField(("ward_description"), default='Ward description...', blank=True, null=True)


	def __str__(self):
		return str(self.ward_name)



class State(models.Model):

	state_id = models.IntegerField(("state_id"))
	state_name = models.CharField(("state_name"), max_length=200)

	def __str__(self):
		return str(self.state_name)



class Party(models.Model):

	party_id = models.CharField(("party_id"), max_length=200)
	party_name = models.CharField(("party_name"), max_length=200)

	def __str__(self):
		return str(self.party_name)