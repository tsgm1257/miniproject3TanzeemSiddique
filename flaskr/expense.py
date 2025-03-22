from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('expense', __name__)

@bp.route('/')
@login_required
def index():
    db = get_db()
    expenses = db.execute(
        'SELECT e.id, e.amount, e.description, e.date, c.name as category'
        ' FROM expense e'
        ' JOIN category c ON e.category_id = c.id'
        ' WHERE e.user_id = ?'
        ' ORDER BY e.date DESC',
        (g.user['id'],)
    ).fetchall()
    return render_template('expense/index.html', expenses=expenses)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    db = get_db()
    categories = db.execute('SELECT * FROM category').fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        category_id = request.form['category']
        error = None

        if not amount or not category_id:
            error = 'Amount and category are required.'

        if error:
            flash(error)
        else:
            db.execute(
                'INSERT INTO expense (user_id, category_id, amount, description) VALUES (?, ?, ?, ?)',
                (g.user['id'], category_id, amount, description)
            )
            db.commit()
            return redirect(url_for('expense.index'))

    return render_template('expense/create.html', categories=categories)

def get_expense(id, check_owner=True):
    expense = get_db().execute(
        'SELECT e.id, e.amount, e.description, e.date, e.user_id, c.name as category'
        ' FROM expense e'
        ' JOIN category c ON e.category_id = c.id'
        ' WHERE e.id = ?',
        (id,)
    ).fetchone()

    if expense is None:
        abort(404, f"Expense id {id} doesn't exist.")

    if check_owner and expense['user_id'] != g.user['id']:
        abort(403)

    return expense

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    expense = get_expense(id)
    db = get_db()
    categories = db.execute('SELECT * FROM category').fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        category_id = request.form['category']
        error = None

        if not amount or not category_id:
            error = 'Amount and category are required.'

        if error:
            flash(error)
        else:
            db.execute(
                'UPDATE expense SET amount = ?, description = ?, category_id = ? WHERE id = ?',
                (amount, description, category_id, id)
            )
            db.commit()
            return redirect(url_for('expense.index'))

    return render_template('expense/update.html', expense=expense, categories=categories)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_expense(id)
    db = get_db()
    db.execute('DELETE FROM expense WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('expense.index'))
