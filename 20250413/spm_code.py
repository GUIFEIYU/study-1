import sentencepiece as spm

# 引入外部文本资料训练分词模型
# spm.SentencePieceTrainer.Train(input='lldq.txt',
#                                model_prefix='lldq_mod',
#                                vocab_size=3989) # Train the model_prefix

# 加载模型进行分词
sp = spm.SentencePieceProcessor(model_file='lldq_mod.model')
# 测试分词
print(sp.EncodeAsPieces('我当然不在意，于是我和加代子一起在冰冻的太平洋上走完了剩下的漫长路程。经过夏威夷后，我们看到了天边的曙光。在被那个小小的太阳照亮的无际冰原上，我们向联合政府的民政部发去了结婚申请')) # 分词