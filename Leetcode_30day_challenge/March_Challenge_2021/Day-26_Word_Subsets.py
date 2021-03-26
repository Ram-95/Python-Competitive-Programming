def wordSubsets(self, A, B):
        count = collections.Counter()
        for b in B:
            count |= collections.Counter(b)
        return [a for a in A if not count - Counter(a)]
