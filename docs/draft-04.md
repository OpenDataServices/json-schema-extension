# Draft 4

The [draft 4 metaschema patch](../schema/draft-04/patch/metaschema-patch.json) sets [`additionalProperties`](https://json-schema.org/understanding-json-schema/reference/object#additionalproperties) to `false` and adds the following properties to [JSON Schema draft 4](https://json-schema.org/specification-links#draft-4).

```{tip}
To reference the extended metaschema, use its canonical URI:

[`http://json-schema-extension.opendataservices.coop/1__0__0/draft-04/metaschema.json`](http://json-schema-extension.opendataservices.coop/1__0__0/draft-04/metaschema.json)
```

```{note}
The patch adds the [`$ref`](https://json-schema.org/understanding-json-schema/structuring#dollarref) keyword which is implemented in JSON Schema draft 4, but missing from the metaschema.
```

```{jsonschema} ../schema/draft-04/patch/metaschema-patch.json
:pointer:
:collapse: deprecatedDetails,deprecated
```

## deprecatedDetails

```{jsoninclude-quote} ../schema/draft-04/patch/metaschema-patch.json
:jsonpointer: /definitions/deprecatedDetails/description
```

```{jsonschema} ../schema/draft-04/patch/metaschema-patch.json
:pointer: /definitions/deprecatedDetails
```