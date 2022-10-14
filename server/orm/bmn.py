# coding: utf-8
from server import db

class Run(db.Model):
    __tablename__ = 'run_'
    __bind_key__ = 'bmn'

    period_number = db.Column(db.ForeignKey('run_period.period_number', onupdate='CASCADE'), primary_key=True, nullable=False)
    run_number = db.Column(db.Integer, primary_key=True, nullable=False)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime)
