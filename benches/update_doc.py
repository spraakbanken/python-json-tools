from json_tools.iter import json_iter


def main():
    data_source = json_iter.load_from_file('benches/data/skbl.json')
    def doc_update(doc):
        doc['_source']['lexiconName'] = 'skbl2'
        doc['_source']['lexiconOrder'] = 48
        return doc
    update_data = (doc_update(doc) for doc in data_source)
    json_iter.dump_to_file(update_data, 'benches/data/skbl2.json')


if __name__ == '__main__':
    main()
