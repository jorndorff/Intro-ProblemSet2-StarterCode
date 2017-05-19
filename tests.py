from unittest import TestCase
import ps2
from timeout_decorator import timeout


class TestInsertionSort(TestCase):
  
  @timeout(5)
  def test_positives(self):
    l = [54, 4, 90, 2, 1, 9, 299]
    ps2.insertion_sort(l)
    self.assertEqual(l, [1, 2, 4, 9, 54, 90, 299])
  
  @timeout(5)
  def test_mixed(self):
    l = [-54, 4, -90, 2, 0, 9, 299]
    ps2.insertion_sort(l)
    self.assertEqual(l, [-90, -54, 0, 2, 4, 9, 299])
  
  @timeout(5) 
  def test_all_same(self):
    l = [1, 1, 1, 1]
    ps2.insertion_sort(l)
    self.assertEqual(l, [1, 1, 1, 1])
  
  @timeout(5)
  def test_empty(self):
    l = []
    ps2.insertion_sort(l)
    self.assertEqual(l, [])
    
class TestAddVariable(TestCase):
  
  @timeout(5)
  def test_n1_longer(self):
    n1 = [1, 2, 3, 4]
    n2 = [2, 3]
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [1, 2, 5, 7])
  
  @timeout(5)  
  def test_n2_longer(self):
    n1 = [2, 3, 5]
    n2 = [1, 2, 3, 4]
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [1, 4, 6, 9])
  @timeout(5)  
  def test_n1_empty(self):
    n1 = []
    n2 = [2, 3]
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [2, 3])
  
  @timeout(5)
  def test_n2_empty(self):
    n1 = [4, 5, 6, 7]
    n2 = []
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [4, 5, 6, 7])
  
  @timeout(5)  
  def test_carry(self):
    n1 = [1, 9, 9]
    n2 = [1, 2, 3]
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [3, 2, 2])
  
  @timeout(5)
  def test_carry_out(self):
    n1 = [9, 5]
    n2 = [2, 3]
    
    ans = ps2.add_variable(n1, n2)
    self.assertEqual(ans, [1, 1, 8])
  
  
class TestSpamFilter(TestCase):

  @timeout(5)
  def setUp(self):
    self.badWords = ["spam", "scam", "nigerian"]

  @timeout(5)
  def test_all_clean(self):
    messages = ["hello", "what's up", "I like cheese"]
    clean = ps2.spam_filter(messages, self.badWords)
    
    self.assertEqual(clean, messages)

  @timeout(5)
  def test_some_clean(self):
    messages = ["hello", "what's up spam", "I like cheese"]
    clean = ps2.spam_filter(messages, self.badWords)
    
    self.assertEqual(clean, ["hello", "I like cheese"])
  
  @timeout(5)  
  def test_some_clean_some_masked(self):
    messages = ["h$$%ello", "nigeria$n prin#@ce", "I like cheese"]
    clean = ps2.spam_filter(messages, self.badWords)
    
    self.assertEqual(clean, ["h$$%ello", "I like cheese"])
  
  @timeout(5)  
  def test_all_spam(self):
    messages = ['spam', 'spam', 'this is a scam']
    clean = ps2.spam_filter(messages, self.badWords)
    
    self.assertEqual(clean, [])
  
  @timeout(5)  
  def test_messages_empty(self):
    clean = ps2.spam_filter([], self.badWords)
    
    self.assertEqual(clean, [])
  
  @timeout(5)  
  def test_bad_words_empty(self):
    messages = ["hello", "what's up spam", "I like cheese"]
    clean = ps2.spam_filter(messages, [])
    
    self.assertEqual(clean, messages)


class TestMergeLists(TestCase):
  
  @timeout(5)
  def test_both_empty(self):
    ans = ps2.merge_lists([], [])
    
    self.assertEqual(ans, [])
  
  @timeout(5)  
  def test_l1_shorter(self):
    l1 = [1, 2, 5]
    l2 = [2, 3, 9, 18, 19]
    ans = ps2.merge_lists(l1, l2)
    self.assertEqual(ans, [1, 2, 2, 3, 5, 9, 18, 19])
    
  @timeout(5)  
  def test_l2_shorter(self):
    l1 = [2, 3, 9, 18, 19]
    l2 = [1, 2, 5]
    ans = ps2.merge_lists(l1, l2)
    self.assertEqual(ans, [1, 2, 2, 3, 5, 9, 18, 19])

  @timeout(5)
  def test_largest_in_shorter(self):
    l1 = [1, 2, 25]
    l2 = [2, 3, 9, 18, 19]
    ans = ps2.merge_lists(l1, l2)
    self.assertEqual(ans, [1, 2, 2, 3, 9, 18, 19, 25])
  
  @timeout(5)  
  def test_same_length(self):
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    ans = ps2.merge_lists(l1, l2)
    self.assertEqual(ans, [1, 2, 3, 4, 5, 6])
  

class TestIsFib(TestCase):

  @timeout(5)
  def test_zero(self):
    f = ps2.is_fib([0])
    self.assertTrue(f)
  
  @timeout(5)  
  def test_zero_one(self):
    f = ps2.is_fib([0, 1])
    self.assertTrue(f)
  
  @timeout(5)  
  def test_nonfib_short_1(self):
    f = ps2.is_fib([4])
    self.assertFalse(f)
  
  @timeout(5)  
  def test_nonfib_short_2(self):
    f = ps2.is_fib([0, 3])
    self.assertFalse(f)
  
  @timeout(5)  
  def test_fib(self):
    f = ps2.is_fib([0, 1, 1, 2, 3, 5, 8])
    self.assertTrue(f)
  
  @timeout(5)  
  def test_nonfib_long(self):
    f = ps2.is_fib([0, 1, 1, 2, 3, 4])
    self.assertFalse(f)
    
    
class TestWordFreq(TestCase):
  
  @timeout(5)
  def test_empty(self):
    f = ps2.word_freq("empty.txt")
    self.assertEqual(f, {})
  
  @timeout(5)
  def test_one_word(self):
    f = ps2.word_freq("oneWord.txt")
    self.assertEqual(f, {'corn': 6})
  
  @timeout(5)
  def test_two_words(self):
    f = ps2.word_freq("twoWords.txt")
    self.assertEqual(f, {'corn': 6, 'cheese': 1})
    
    

class TestTenGreatest(TestCase):

  # Promised kids in spring 2016 I wouldn't test dicts with fewer than 10 items
  #TODO should probably make this 5 greatest next time around so the test cases aren't such a pain.
  
  @timeout(5)
  def test_standard(self):
    d = {'a':4, 'b':5, 'c':6, 'd':7, 'e':8, 'f':9, 'g':10, 'h':11, 'i':12, 'j':13, 'k':14}
         
    a = sorted(ps2.ten_greatest(d))
    correct = sorted(['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_some_negative(self):
    d = {'a':-4, 'b':-5, 'c':-6, 'd':-7, 'e':8, 'f':9, 'g':10, 'h':11, 'i':12, 'j':13, 'k':14}
         
    a = sorted(ps2.ten_greatest(d))
    correct = sorted(['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_some_tied(self):
    d = {'a':1, 'b':1, 'c':1, 'd':0, 'e':1, 'f':2, 'g':1, 'h':1, 'i':1, 'j':1, 'k':1}
         
    a = sorted(ps2.ten_greatest(d))
    correct = sorted(['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_always_ten(self):
    d = {'a':0, 'b':1, 'c':1, 'd':0, 'e':1, 'f':2, 'g':2, 'h':1, 'i':1, 'j':1, 'k':1}
         
    a = ps2.ten_greatest(d)
    self.assertEqual(len(a), 10)
  

class TestValidate5K(TestCase):

  @timeout(5)
  def test_empty(self):
    a = ps2.validate_5k([])
    
    self.assertEqual(a, {})
  
  @timeout(5) 
  def test_standard(self):
    d = [("Josh", "17.59"), ("Aye", "22.34"), ("Davidson", "20.00")]
    
    a = ps2.validate_5k(d)
    correct = {"Josh": "17.59", "Aye": "22.34", "Davidson": "20.00"}
    
    self.assertEqual(a, correct)

  @timeout(5)
  def test_bad_name(self):
    d = [("J", "17.59"), ("Aye", "22.34"), ("Davidson", "20.00")]
    
    a = ps2.validate_5k(d)
    correct = {"Aye": "22.34", "Davidson": "20.00"}
    
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_bad_time(self):
    d = [("Josh", "17.69"), ("Aye", "22.34"), ("Davidson", "20.00")]
    
    a = ps2.validate_5k(d)
    correct = {"Aye": "22.34", "Davidson": "20.00"}
    
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_all_bad(self):
    d = [("J", "17.59"), ("Aye", "22.74"), ("D", "20.99")]
    
    a = ps2.validate_5k(d)
    
    self.assertEqual(a, {})
    

class TestXor(TestCase):

  @timeout(5)
  def test_no_overlap(self):
    l1 = [1, 3, 5]
    l2 = [7, 8, 9]
    
    a = sorted(ps2.xor(l1, l2))
    correct = sorted([1, 3, 5, 7, 8, 9])
    
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_all_overlap(self):
    l1 = [1, 3, 5]
    l2 = [3, 1, 5]
    
    a = ps2.xor(l1, l2)
    
    self.assertEqual(a, [])
  
  @timeout(5)
  def test_some_overlap(self):
    l1 = [1, 3, 5]
    l2 = [7, 1, 9]
    
    a = sorted(ps2.xor(l1, l2))
    correct = sorted([3, 5, 7, 9])
    
    self.assertEqual(a, correct)
  
  @timeout(5)
  def test_l1_empty(self):
    l1 = []
    l2 = [7, 8, 9]
    
    a = sorted(ps2.xor(l1, l2))
    
    self.assertEqual(a, [7, 8, 9])
  
  @timeout(5)
  def test_l2_empty(self):
    l1 = [1, 3, 5]
    l2 = []
    
    a = sorted(ps2.xor(l1, l2))
    
    self.assertEqual(a, [1, 3, 5])
  
  @timeout(5)
  def test_both_empty(self):
    l1 = []
    l2 = []
    
    a = ps2.xor(l1, l2)
    
    self.assertEqual(a, [])
    
    
