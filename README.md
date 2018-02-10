SimpleQuestionsWikidata
==========================

This repository provides a version of the [SimpleQuestions](https://research.fb.com/downloads/babi/) dataset mapped to Wikidata.

## Description

Data is organized in 6 files: `annotated_wd_data_{train, valid, test}{_full}.txt` .
Each file contains one example per line with the following format:
`subject [tab] property [tab] object [tab] question`, with `subject`, `property` and `object` being identifiers of Wikidata items or properties.
`Rxxx` property identifiers encode the inverse property of the Wikidata property `Pxxx`. For example `R19` encodes the properties "born here", i.e. the inverse of `P19` ("birth place"). Note that not every translated triple must also exist in Wikidata. Part of the information when moving from Freebase to Wikidata was lost. The files ending with "_answerable" contain only triples that are also in Wikidata.

The mapping code is in the `build.ipynb` file. The mapping of Freebase topics to Wikidata items is done using the `mid_to_qid.tsv` file and the one between properties is the one [stored on Wikidata](https://www.wikidata.org/wiki/Wikidata:WikiProject_Freebase/Mapping). Contributions to these mappings are welcome.

* `annotated_wd_data_train.txt` contains 34374 questions converted from the 75910 original questions.
* `annotated_wd_data_test.txt` contains 9961 questions converted from the 21687 original questions.
* `annotated_wd_data_valid.txt` contains 4867 questions converted from the 10845 original questions.

* `annotated_wd_data_train_answerable.txt` contains 14695 questions converted from the 75910 original questions.
* `annotated_wd_data_test_answerable.txt` contains 4249 questions converted from the 21687 original questions.
* `annotated_wd_data_valid_answerable.txt` contains 2013 questions converted from the 10845 original questions.

You can find the same datasets also in the QALD format in the QALD-format directory.

## Publication

If you use this dataset please cite:

Question Answering Benchmarks for Wikidata 
by Diefenbach, Dennis and Tanon, Thomas and Singh, Kamal and Maret, Pierre
ISWC 2017

BibTeX:
```
@inproceedings{wikidata-benchmark,
  author    = {Dennis Diefenbach and
               Thomas Pellissier Tanon and
               Kamal Deep Singh and
               Pierre Maret},
  title     = {Question Answering Benchmarks for Wikidata},
  booktitle = {Proceedings of the {ISWC} 2017 Posters {\&} Demonstrations and
               Industry Tracks co-located with 16th International Semantic Web Conference
               {(ISWC} 2017), Vienna, Austria, October 23rd - to - 25th, 2017.},
  year      = {2017},
  url       = {http://ceur-ws.org/Vol-1963/paper555.pdf}
}
```
