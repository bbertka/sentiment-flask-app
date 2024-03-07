#!/usr/bin/python3

from flask import Flask, jsonify, request

import scrape as scraper
import analyze as analyzer

app = Flask(__name__)

@app.route('/sentiment', methods=['GET'])
def sentiment():
    item = request.args.get('item')
    code = 200
    response = {
        'item': item,
        'sentiment': '',
        'result': ''
    }

    try:
        df = scraper.scrape(item)
    except Exception as e:
        code = 500
        response = {
            'item': item,
            'sentiment': '',
            'result': "error scraping: %s" % str(e)
        }
        return jsonify(response), code

    try:
        verdict, result = analyzer.interprete(df, thresh=[1.75, 2.25] )
        if verdict and result:
            code = 200
            response = {
                'item': item,
                'sentiment': verdict,
                'result': result
            }
            print("Avg. Sentiment Rating for this Product: %s (%f)" % (verdict, result) )
            return jsonify(response), code
        else:
            print("error: analyzer: unable to fetch results")
            code = 500
            response = {
                'item': item,
                'sentiment': '',
                'result': "Unknown error: analyzer: unable to fetch results"
            }
            return jsonify(response), code
    except Exception as e:
            code = 500
            response = {
                'item': item,
                'sentiment': '',
                'result': "error: %s" % str(e)
            }

    return jsonify(response), code


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
