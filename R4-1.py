def find_max(S):
	def find_m(S, stop):
		if stop == 0:
			return S[stop]
		else:
			return max(S[stop],find_m(S, stop-1))
	return find_m(S, len(S) - 1)

