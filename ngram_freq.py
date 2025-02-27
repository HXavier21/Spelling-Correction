from collections import Counter
from itertools import chain

# 定义输入文件名和输出文件名
input_file_name = 'reuters_sentences.txt'
output_file_name = 'reuters_ngram_frequencies.txt'

# 读取文件中的句子
with open(input_file_name, 'r', encoding='utf-8') as infile:
    sentences = infile.readlines()

# 将每个句子合并为一个大字符串
corpus = ' '.join(sentences)

# 分词
words = corpus.split()

# 定义ngrams函数
def ngrams(sequence, n, pad_left=False, pad_right=False, left_pad_symbol=None, right_pad_symbol=None):
    sequence = iter(sequence)
    if pad_left:
        sequence = chain((left_pad_symbol,) * (n - 1), sequence)
    if pad_right:
        sequence = chain(sequence, (right_pad_symbol,) * (n - 1))
    history = []
    while n > 1:
        try:
            next_item = next(sequence)
        except StopIteration:
            return
        history.append(next_item)
        n -= 1
    for item in sequence:
        history.append(item)
        yield tuple(history)
        history.pop(0)


# 生成各阶n-gram
uni_grams = list(ngrams(words, 1))
bi_grams = list(ngrams(words, 2))
tri_grams = list(ngrams(words, 3))

# 计算各阶n-gram频率
uni_gram_freq = Counter(uni_grams)
bi_gram_freq = Counter(bi_grams)
tri_gram_freq = Counter(tri_grams)

# 保存结果到文件
with open(output_file_name, 'w', encoding='utf-8') as outfile:
    outfile.write("Unigram Frequencies:\n")
    for uni_gram, freq in uni_gram_freq.items():
        outfile.write(f"{uni_gram}\t{freq}\n")

    outfile.write("\nBigram Frequencies:\n")
    for bi_gram, freq in bi_gram_freq.items():
        outfile.write(f"{bi_gram}\t{freq}\n")

    outfile.write("\nTrigram Frequencies:\n")
    for tri_gram, freq in tri_gram_freq.items():
        outfile.write(f"{tri_gram}\t{freq}\n")

print(f"N-gram frequencies have been saved to '{output_file_name}'.")