# coding: utf-8
from server import db


t_att_array_devboolean_ro = db.Table(
    'att_array_devboolean_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devboolean_rw = db.Table(
    'att_array_devboolean_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devdouble_ro = db.Table(
    'att_array_devdouble_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float(asdecimal=True)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devdouble_rw = db.Table(
    'att_array_devdouble_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float(asdecimal=True)),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Float(asdecimal=True)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devencoded_ro = db.Table(
    'att_array_devencoded_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.LargeBinary),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devencoded_rw = db.Table(
    'att_array_devencoded_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.LargeBinary),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.LargeBinary),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devfloat_ro = db.Table(
    'att_array_devfloat_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devfloat_rw = db.Table(
    'att_array_devfloat_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Float),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devlong64_ro = db.Table(
    'att_array_devlong64_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devlong64_rw = db.Table(
    'att_array_devlong64_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devlong_ro = db.Table(
    'att_array_devlong_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devlong_rw = db.Table(
    'att_array_devlong_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devshort_ro = db.Table(
    'att_array_devshort_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devshort_rw = db.Table(
    'att_array_devshort_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devstate_ro = db.Table(
    'att_array_devstate_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devstate_rw = db.Table(
    'att_array_devstate_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devstring_ro = db.Table(
    'att_array_devstring_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.String(16384)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devstring_rw = db.Table(
    'att_array_devstring_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.String(16384)),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.String(16384)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devuchar_ro = db.Table(
    'att_array_devuchar_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devuchar_rw = db.Table(
    'att_array_devuchar_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devulong64_ro = db.Table(
    'att_array_devulong64_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devulong64_rw = db.Table(
    'att_array_devulong64_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devulong_ro = db.Table(
    'att_array_devulong_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devulong_rw = db.Table(
    'att_array_devulong_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devushort_ro = db.Table(
    'att_array_devushort_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_array_devushort_rw = db.Table(
    'att_array_devushort_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('idx', db.Integer, nullable=False),
    db.Column('dim_x_r', db.Integer, nullable=False),
    db.Column('dim_y_r', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('dim_x_w', db.Integer, nullable=False),
    db.Column('dim_y_w', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_w', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



class AttConf(db.Model):
    __tablename__ = 'att_conf'
    __bind_key__ = 'hdbpp'

    att_conf_id = db.Column(db.Integer, primary_key=True)
    att_name = db.Column(db.String(255), nullable=False, unique=True)
    att_conf_data_type_id = db.Column(db.Integer, nullable=False, index=True)
    facility = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    domain = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    family = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    member = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())



class AttConfDataType(db.Model):
    __tablename__ = 'att_conf_data_type'
    __bind_key__ = 'hdbpp'

    att_conf_data_type_id = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(255), nullable=False)
    tango_data_type = db.Column(db.Integer, nullable=False)



t_att_history = db.Table(
    'att_history',
    db.Column('att_conf_id', db.Integer, nullable=False, index=True),
    db.Column('time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('att_history_event_id', db.Integer, nullable=False, index=True),
    info={'bind_key': 'hdbpp'}
)



class AttHistoryEvent(db.Model):
    __tablename__ = 'att_history_event'
    __bind_key__ = 'hdbpp'

    att_history_event_id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255), nullable=False)



t_att_parameter = db.Table(
    'att_parameter',
    db.Column('att_conf_id', db.Integer, nullable=False, index=True),
    db.Column('recv_time', db.DateTime, nullable=False, index=True, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('label', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('unit', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('standard_unit', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('display_unit', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('format', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('archive_rel_change', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('archive_abs_change', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('archive_period', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('description', db.String(255), nullable=False, server_default=db.FetchedValue()),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devboolean_ro = db.Table(
    'att_scalar_devboolean_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devboolean_rw = db.Table(
    'att_scalar_devboolean_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devdouble_ro = db.Table(
    'att_scalar_devdouble_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float(asdecimal=True)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devdouble_rw = db.Table(
    'att_scalar_devdouble_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float(asdecimal=True)),
    db.Column('value_w', db.Float(asdecimal=True)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devencoded_ro = db.Table(
    'att_scalar_devencoded_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.LargeBinary),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devencoded_rw = db.Table(
    'att_scalar_devencoded_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.LargeBinary),
    db.Column('value_w', db.LargeBinary),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devfloat_ro = db.Table(
    'att_scalar_devfloat_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devfloat_rw = db.Table(
    'att_scalar_devfloat_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Float),
    db.Column('value_w', db.Float),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devlong64_ro = db.Table(
    'att_scalar_devlong64_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devlong64_rw = db.Table(
    'att_scalar_devlong64_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('value_w', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devlong_ro = db.Table(
    'att_scalar_devlong_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devlong_rw = db.Table(
    'att_scalar_devlong_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devshort_ro = db.Table(
    'att_scalar_devshort_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devshort_rw = db.Table(
    'att_scalar_devshort_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('value_w', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devstate_ro = db.Table(
    'att_scalar_devstate_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devstate_rw = db.Table(
    'att_scalar_devstate_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devstring_ro = db.Table(
    'att_scalar_devstring_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.String(16384)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devstring_rw = db.Table(
    'att_scalar_devstring_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.String(16384)),
    db.Column('value_w', db.String(16384)),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devuchar_ro = db.Table(
    'att_scalar_devuchar_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devuchar_rw = db.Table(
    'att_scalar_devuchar_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devulong64_ro = db.Table(
    'att_scalar_devulong64_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devulong64_rw = db.Table(
    'att_scalar_devulong64_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.BigInteger),
    db.Column('value_w', db.BigInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devulong_ro = db.Table(
    'att_scalar_devulong_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devulong_rw = db.Table(
    'att_scalar_devulong_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.Integer),
    db.Column('value_w', db.Integer),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devushort_ro = db.Table(
    'att_scalar_devushort_ro',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)



t_att_scalar_devushort_rw = db.Table(
    'att_scalar_devushort_rw',
    db.Column('att_conf_id', db.Integer, nullable=False),
    db.Column('data_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('recv_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('insert_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('value_r', db.SmallInteger),
    db.Column('value_w', db.SmallInteger),
    db.Column('quality', db.Integer),
    db.Column('error_desc', db.String(255)),
    db.Index('att_conf_id_data_time', 'att_conf_id', 'data_time'),
    info={'bind_key': 'hdbpp'}
)
