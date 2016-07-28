import sys
from itertools import chain, combinations
from collections import defaultdict


def dataFromFile(fname):
        """
        Function which reads from the file and yields a generator of frozen sets of each line in the csv

        The first line of tesco.csv file returns the following output:
        frozenset(['beer', 'rice', 'apple', 'chicken'])
        """
        file_iter = open(fname, 'rU')
        for line in file_iter:
                line = line.strip().rstrip(',')                         # Remove trailing comma
                record = frozenset(line.split(','))
                yield record


def getItemSetTransactionList(data_iterator):
		"""
		Takes data from dataFromFile() and returns list of items and a list of transactions
		and generate two seperate sets of items and transactions.

		The item list would be: 
		([frozenset(['apple']), frozenset(['beer']), frozenset(['chicken']), etc

		The transaction list would be:
		frozenset(['beer', 'rice', 'apple', 'chicken']), frozenset(['beer', 'rice', 'apple']), etc
		"""
		transactionList = list()
		itemSet = set()
		for record in data_iterator:
			transaction = record
			transactionList.append(transaction)
			for item in transaction:
				itemSet.add(frozenset([item]))              # Generate 1-itemSets            
		
		return itemSet, transactionList




def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
        """
        calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support

       Takes the itemset and transactionList from getItemSetTransactionList() method
       and returns a list of items whose elements satisfies minimum support.

       """
        _itemSet = set()
        localSet = defaultdict(int)

        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)

                if support >= minSupport:
                        _itemSet.add(item)

        return _itemSet


def joinSet(itemSet, length):
        """Join a set with itself and returns the n-element itemsets"""
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])

a = set([frozenset(['apple']), frozenset(['beer']), frozenset(['chicken']), frozenset(['mango']), frozenset(['milk']), frozenset(['rice'])])
print joinSet(a, 3)

#print getItemSetTransactionList(dataFromFile("tesco.csv"))


