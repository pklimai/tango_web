# coding: utf-8
from server import db


class Detector(db.Model):
    __tablename__ = 'detector_'
    __bind_key__ = 'bmn'

    detector_name = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String(30))



class DetectorParameter(db.Model):
    __tablename__ = 'detector_parameter'
    __bind_key__ = 'bmn'
    __table_args__ = (
        db.ForeignKeyConstraint(['end_period', 'end_run'], ['run_.period_number', 'run_.run_number']),
        db.ForeignKeyConstraint(['start_period', 'start_run'], ['run_.period_number', 'run_.run_number'])
    )

    value_id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    detector_name = db.Column(db.ForeignKey('detector_.detector_name'), nullable=False)
    parameter_id = db.Column(db.ForeignKey('parameter_.parameter_id'), nullable=False)
    start_period = db.Column(db.Integer, nullable=False)
    start_run = db.Column(db.Integer, nullable=False)
    end_period = db.Column(db.Integer, nullable=False)
    end_run = db.Column(db.Integer, nullable=False)
    dc_serial = db.Column(db.BigInteger)
    channel = db.Column(db.Integer)
    parameter_value = db.Column(db.LargeBinary, nullable=False)

    detector_ = db.relationship('Detector', primaryjoin='DetectorParameter.detector_name == Detector.detector_name', backref='detector_parameters')
    run_ = db.relationship('Run', primaryjoin='and_(DetectorParameter.end_period == Run.period_number, DetectorParameter.end_run == Run.run_number)', backref='run_detector_parameters')
    parameter = db.relationship('Parameter', primaryjoin='DetectorParameter.parameter_id == Parameter.parameter_id', backref='detector_parameters')
    run_1 = db.relationship('Run', primaryjoin='and_(DetectorParameter.start_period == Run.period_number, DetectorParameter.start_run == Run.run_number)', backref='run_detector_parameters_0')



class Parameter(db.Model):
    __tablename__ = 'parameter_'
    __bind_key__ = 'bmn'

    parameter_id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    parameter_name = db.Column(db.String(20), nullable=False, unique=True)
    parameter_type = db.Column(db.Integer, nullable=False)



class Run(db.Model):
    __tablename__ = 'run_'
    __bind_key__ = 'bmn'
    __table_args__ = (
        db.CheckConstraint('energy > (0)::double precision'),
        db.CheckConstraint('event_count >= 0'),
        db.CheckConstraint('file_size > (0)::double precision')
    )

    period_number = db.Column(db.ForeignKey('run_period.period_number', onupdate='CASCADE'), primary_key=True, nullable=False)
    run_number = db.Column(db.Integer, primary_key=True, nullable=False)
    file_path = db.Column(db.String(200), nullable=False, unique=True)
    beam_particle = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue())
    target_particle = db.Column(db.String(10))
    energy = db.Column(db.Float(53))
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime)
    event_count = db.Column(db.Integer)
    field_voltage = db.Column(db.Float(53))
    file_size = db.Column(db.Float(53))
    geometry_id = db.Column(db.ForeignKey('run_geometry.geometry_id', onupdate='CASCADE'))

    geometry = db.relationship('RunGeometry', primaryjoin='Run.geometry_id == RunGeometry.geometry_id', backref='runs')
    run_period = db.relationship('RunPeriod', primaryjoin='Run.period_number == RunPeriod.period_number', backref='runs')



class RunGeometry(db.Model):
    __tablename__ = 'run_geometry'
    __bind_key__ = 'bmn'

    geometry_id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    root_geometry = db.Column(db.LargeBinary, nullable=False)



class RunPeriod(db.Model):
    __tablename__ = 'run_period'
    __bind_key__ = 'bmn'

    period_number = db.Column(db.Integer, primary_key=True)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime)



class SimulationFile(db.Model):
    __tablename__ = 'simulation_file'
    __bind_key__ = 'bmn'
    __table_args__ = (
        db.CheckConstraint('energy > (0)::double precision'),
        db.CheckConstraint('event_count >= 0'),
        db.CheckConstraint('file_size > (0)::double precision')
    )

    file_id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    file_path = db.Column(db.String(200), nullable=False, unique=True)
    generator_name = db.Column(db.String(20), nullable=False)
    beam_particle = db.Column(db.String(10), nullable=False)
    target_particle = db.Column(db.String(10))
    energy = db.Column(db.Float(53))
    centrality = db.Column(db.String(10), nullable=False)
    event_count = db.Column(db.Integer)
    file_desc = db.Column(db.String(30))
    file_size = db.Column(db.Float(53))
