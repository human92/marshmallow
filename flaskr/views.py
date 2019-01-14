from flask import request, redirect, url_for, render_template, flash, jsonify
from flaskr import app, db, ma
from flaskr.models import Entry
from flaskr.models import EntrySchema

#ブラウザから見れる画面用-------------------------------------------------------
@app.route('/')
def show_entries():
        entries = Entry.query.order_by(Entry.id.desc()).all()
        return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
        entry = Entry(
                title=request.form['title'],
                text=request.form['text']
                )
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))

#json変換用(API)----------------------------------------------------------------
@app.route('/api', methods=['POST'])
def show_entries_json():
        entries = Entry.query.order_by(Entry.id.desc()).all()
        entries_schema = EntrySchema(many=True)
        return jsonify({'entries': entries_schema.dump(entries).data})