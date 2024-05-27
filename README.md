# IMPROVE_L1_interference
В данном репозитории находятся материалы, относящиеся к курсовой работе на тему "Усовершенствование нейросетевых методов поиска ошибок под влиянием языковой интерференции в учебных текстах: переразметка и аугментация данных, поиск оптимальной архитектуры"

Все перечисленные здесь модели могут быть загружены с сайта huggingface и использованы в библиотеке SpaCy или transformers. Чтобы использовать модель, необходимо перейти на ее страницу по ссылке из списка ниже и следовать инструкциям, доступным после нажатия кнопки `Deploy`.

Ссылки на результирующие модели на huggingface:

Классификаторы ошибок (SpaCy):
 - [en_L1_Rulegen_spanbert](https://huggingface.co/Zlovoblachko/en_L1_Rulegen_spanbert)
 - [en_L1_Fullgen_spanbert](https://huggingface.co/Zlovoblachko/en_L1_Fullgen_spanbert)
 - [en_L1_RuleGen_xlm](https://huggingface.co/Zlovoblachko/en_L1_RuleGen_xlm)
 - [en_L1_FullGen_xlm](https://huggingface.co/Zlovoblachko/en_L1_FullGen_xlm)
 - [en_L1_FullGen_large](https://huggingface.co/Zlovoblachko/en_L1_FullGen_large)
 - [en_L1_RuleGen_large](https://huggingface.co/Zlovoblachko/en_ppline)
 - [en_L1_FullGen_base](https://huggingface.co/Zlovoblachko/en_ouroboros2)

Генераторы ошибок по типам (доступны в Inference API на сайте HF) (transformers):
 - [TenSem_L1_sent_generator](https://huggingface.co/Zlovoblachko/TenSem_L1_sent_generator)
 - [WFT_L1_sent_generator](https://huggingface.co/Zlovoblachko/WFT_L1_sent_generator)
 - [Transliteration_L1_sent_generator](https://huggingface.co/Zlovoblachko/Transliteration_L1_sent_generator)
 - [CopExp_L1_sent_generator](https://huggingface.co/Zlovoblachko/CopExp_L1_sent_generator)
 - [Synonyms_L1_sent_generator](https://huggingface.co/Zlovoblachko/Synonyms_L1_sent_generator)

Базовые генераторы (transformers):
 - [GPT2_L1_sent_generator](https://huggingface.co/Zlovoblachko/GPT2_L1_sent_generator)
 - [test_L1_sent_generator](https://huggingface.co/Zlovoblachko/test_L1_sent_generator)

Классификаторы предложений по наличию/отсутствию в них ошибок (transformers):
 - [L1-classifier-Transliteration](https://huggingface.co/Zlovoblachko/L1-classifier-Transliteration)
 - [L1-classifier-Synonyms](https://huggingface.co/Zlovoblachko/L1-classifier-Synonyms)
 - [L1-classifier-WFT](https://huggingface.co/Zlovoblachko/L1-classifier-WFT)
 - [L1-classifier-CopExp](https://huggingface.co/Zlovoblachko/L1-classifier-CopExp)
 - [L1-classifier-TenSem](https://huggingface.co/Zlovoblachko/L1-classifier-TenSem)
