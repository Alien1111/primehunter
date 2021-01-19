def main():
#this code is not pep8 compliant
#if that bothers you, FUCK OFF!
	from math import sqrt
	from time import sleep
	print("Return 'yes' for positive answer.")
	print("To enter settings return 'set'.")
	positiveanswer = {'yes', 'y', 'Y', 'positive', 'Yes', 'YES', 'ja', 'ok',
	'OK', 'Ok', 'Ja', 'JA', 'Positive', '+', 'POSITIVE', 'Yes.', 'da', 'Da',
	'yep', 'aha'}

	def leave():
		print('Then fuck off!')
		sleep(2)
		quit()


#this funcion list out primes
#can be used for a specific number of primes
#or up to a certain number
	def primefinder():
		primes = [2]
		foundcounter = 1
		if maxnumberofnumberschecked > 1:
			print('1. prime:   2')
			for i in range(3, maxnumberofnumberschecked, 2):
				divisorcounter = 0
				if wantednumberofprimes > 1:
					for p in primes:
						if i%p == 0:
							divisorcounter += 1
							break
						elif (i%p != 0) and (divisorcounter == 0) and (p >= sqrt(i)):
							foundcounter += 1
							print(str(foundcounter) + '. prime:   ' + str(i))
							primes.append(i)
							break
				if foundcounter == wantednumberofprimes:
					break
			print(primes)
		else:
			print('There is no prime up to this value.')
		replayquestion = input('Do you want go give it another go?: ')
		if replayquestion in positiveanswer:
			main()
		else:
			leave()

	def utilityprimefinder(upperlimit):
		primes = [2]
		for i in range(3, int(upperlimit), 2):
			divisorcounter = 0
			for p in primes:
				if i%p == 0:
					divisorcounter += 1
					break
				elif (i%p != 0) and (divisorcounter == 0) and (p >= sqrt(i)):
					primes.append(i)
					break
		return primes


#this function checks if the inputted number is a prime or not
	def primechecker():
		numbertocheck = int(input('What is the number you want to check?: '))
		primes = utilityprimefinder(sqrt(numbertocheck))
		for bp in primes:
			if numbertocheck%bp == 0 or numbertocheck == 1:
				print(str(numbertocheck) + ' IS NOT A PRIME.')
				numberstate = 'notprime'
				break
			else:
				numberstate = 'primefornow'
		divisorcounter = 0
		if numberstate != 'notprime':
			for i in range(7921, int(sqrt(numbertocheck)), 2):
				divisorcounter = 0
				for p in primes:
					if i%p == 0:
						divisorcounter += 1
						break
					elif (i%p != 0) and (divisorcounter == 0) and (p >= sqrt(i)):
						primes.append(i)
					break
			divisorcheck = 0
			for p in primes:
				divisorcheck += 1
				if numbertocheck%p == 0:
					print(str(numbertocheck) + ' IS NOT A PRIME.')
					break
				elif (numbertocheck%p != 0) and divisorcheck == len(primes):
					print(str(numbertocheck) + ' IS A PRIME.')
					break
		replayquestion = input('Do you want go give it another go?: ')
		if replayquestion in positiveanswer:
			main()
		else:
			leave()


#this function is not precise
#it has been ditched
#left it here for reuse
	def nextprime1():
		print('WARNING')
		print('This may not be a 100% precise at very big numbers! A sacrifice for speed.')
		print('WARNING')
		proceed = input('Would you like to proceed?: ')
		if proceed in positiveanswer:
			threshold = int(input('What is your threshold?: '))
			primes = [2]
			state = 0
			for i in range(3, int(sqrt(threshold * 2)), 2):
				if state == 1:
					break
				for p in primes:
					if i%p == 0:
						break
					elif (i%p != 0) and (p >= sqrt(i)):
						primes.append(i)
						break
			finishit = 0
			for i in range(threshold, int(threshold * 2)):
				if finishit == 1:
					break
				for p in primes:
					if i%p == 0:
						break
					elif (i%p != 0) and (p > sqrt(i)):
						print(str(i) + ' is the biggest prime after ' + str(threshold) + '.')
						finishit = 1
						break
			replayquestion = input('Do you want go give it another go?: ')
			if replayquestion in positiveanswer:
				main()
			else:
				leave()
		else:
			main()



#this function finds the smallest prime above an inputted threshold
	def nextprime():
		threshold = int(input('What is your threshold?: '))
		for primecandidate in range(threshold, (threshold**2)):
			finished = 0
			if primecandidate%2 != 0:
				primes = ogprimes
				for bp in primes:
					if primecandidate%bp == 0 or primecandidate == 1:
						numberstate = 'notprime'
						break
					else:
						numberstate = 'primefornow'
				divisorcounter = 0
				if numberstate != 'notprime':
					for i in range(7921, int(sqrt(primecandidate))):
						divisorcounter = 0
						for p in primes:
							if i%p == 0:
								divisorcounter += 1
								break
							elif (i%p != 0) and (divisorcounter == 0) and (p >= sqrt(i)):
								primes.append(i)
							break
					divisorcheck = 0
					for p in primes:
						divisorcheck += 1
						if primecandidate%p == 0:
							print(str(primecandidate) + ' is the next prime after ' + str(threshold) + '.')
							found = 1
							break
						elif (primecandidate%p != 0) and divisorcheck == len(primes):
							print(str(primecandidate))
							finished = 1
							break
			if finished == 1:
				break
		replayquestion = input('Do you want go give it another go?: ')
		if replayquestion in positiveanswer:
			main()
		else:
			leave()


#here are the questions that lead to the functions
	question1 = input('Do you want a specific number of primes?: ')
	if question1 in positiveanswer:
		wantednumberofprimes = int(input('How many primes do you want?: '))
		maxnumberofnumberschecked = 4_294_967_295
		primefinder()
	else:
		question2 = input('Are you looking for primes up to a certain number?: ')
		if question2 in positiveanswer:
			maxnumberofnumberschecked = int(input('What is your upper limit?: '))
			wantednumberofprimes = 4_294_967_295
			primefinder()
		else:
			question3 = input('Do you want to check if a number is a prime?: ')
			if question3 in positiveanswer:
				primechecker()
			else:
				question4 = input('Are you looking for the next prime above a given number?: ')
				if question4 in positiveanswer:
					nextprime()
				else:
					leave()
main()
