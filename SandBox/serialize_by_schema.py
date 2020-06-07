'''
Assignment: Create functions that serialize/deserialize objects to/from a stream of data. Additionally, create a function
that retrieves a given value from the stream of data.

All objects have a flat structure that is described by a schema. Objects needn't have all fields, in such a case, the default
value is assumed. The example of a schema is given below:

schema = [
    {
        "id": "name",
        "default": "<UNNAMED>"
    },
    {
        "id": "width",
        "default": 10
    },
    {
        "id": "height",
        "default": 10
    }
]



-----------------------------------------------------------------------------------------------------------------------
Usage example:
-----------------------------------------------------------------------------------------------------------------------
sample_structured_data = [
    {
        "name": "Rectangle 1",
        "width": 12,
        "height": 20
    },
    {
        "name": "Rectangle 2",
        "height": 20
    },
    {
        "name": "Rectangle 3"
    },
    {
    }
]

sample_serialized_data = ['Rectangle 1', 12, 20, 'Rectangle 2', 10, 20, 'Rectangle 3', 10, 10, '<UNNAMED>', 10, 10]


print(serialize_data(sample_structured_data))
# Prints: ['Rectangle 1', 12, 20, 'Rectangle 2', 10, 20, 'Rectangle 3', 10, 10, '<UNNAMED>', 10, 10]

print(deserialize_data(sample_serialized_data))
# Prints: [{'name': 'Rectangle 1', 'width': 12, 'height': 20}, {'name': 'Rectangle 2', 'width': 10, 'height': 20}, {'name': 'Rectangle 3', 'width': 10, 'height': 10}, {'name': '<UNNAMED>', 'width': 10, 'height': 10}]

print(get_from_serialized_data(sample_serialized_data, "width", 2))
# Prints: 10
'''


schema = [
    {
        "id": "name",
        "default": "<UNNAMED>"
    },
    {
        "id": "width",
        "default": 10
    },
    {
        "id": "height",
        "default": 10
    }
]

schema_len = len(schema)

schema_by_ids = {
    field_schema["id"]: {"idx": field_idx, "default": field_schema["default"]} for field_idx, field_schema in enumerate(schema)
}


def serialize_data(data):
    stream = []

    for record in data:
        for field_schema in schema:
            field_id = field_schema["id"]
            val = record[field_id] if field_id in record else field_schema["default"]
            stream.append(val)

    return stream


def deserialize_data(stream):
    data = []

    records = [stream[i:i + schema_len] for i in range(0, len(stream), schema_len)]

    for record in records:
        output_record = {}

        for val, field_schema in zip(record, schema):
            field_id = field_schema["id"]
            output_record[field_id] = val

        data.append(output_record)

    return data


def get_from_serialized_data(stream, field_id, record_idx):
    field_schema = schema_by_ids[field_id]
    stream_offset = record_idx * schema_len + field_schema["idx"]
    return stream[stream_offset]



sample_structured_data = [
    {
        "name": "Rectangle 1",
        "width": 12,
        "height": 20
    },
    {
        "name": "Rectangle 2",
        "height": 20
    },
    {
        "name": "Rectangle 3"
    },
    {
    }
]

sample_serialized_data = ['Rectangle 1', 12, 20, 'Rectangle 2', 10, 20, 'Rectangle 3', 10, 10, '<UNNAMED>', 10, 10]


print(serialize_data(sample_structured_data))
print(deserialize_data(sample_serialized_data))
print(get_from_serialized_data(sample_serialized_data, "width", 2))