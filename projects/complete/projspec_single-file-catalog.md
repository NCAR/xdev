# Project: Single File Catalog

- [Project: Single File Catalog](#project-single-file-catalog)
  - [Campaigns](#campaigns)
  - [Overview](#overview)
  - [Repositories](#repositories)
  - [Skills & Knowledge](#skills--knowledge)
  - [Deliverables](#deliverables)
    - [esm-collection-spec side](#esm-collection-spec-side)
    - [intake-esm side](#intake-esm-side)
  - [Milestones & Timeline](#milestones--timeline)
  - [References](#references)

## Campaigns

- WORKFLOWS: Ingestion

## Overview

The current spec requires that the `catalog_file` point to a `csv file`. In some cases, it would be useful to embed the catalog "table" in the catalog itself. A so called single-file-catalog. STAC has an extension that does this (see [here](https://github.com/radiantearth/stac-spec/tree/master/extensions/single-file-stac)).

## Repositories

- https://github.com/NCAR/esm-collection-spec
- https://github.com/NCAR/intake-esm

## Skills & Knowledge

- Familiarity with [esm collection specification](https://github.com/NCAR/esm-collection-spec/blob/master/collection-spec/collection-spec.md)

## Deliverables

- Make `catalog_file` key optional and support a key `catalog_dict` which is a json dictionary that represents the data that would otherwise be in the csv. Exactly one of the two keys would be required but the catalog creator could choose.

The `catalog_dict` dictionary can be expressed in two ways:

**Option 1) dict**: dict like ```{column -> {index -> value}}```:

```yaml
{
    "esmcat_version":"0.1.0",
    "id":"aws-cesm1-le",
    "description":"This is an ESM collection for CESM1 Large Ensemble Zarr dataset publicly available on Amazon S3 (us-west-2 region)",
    "catalog_dict":{
        'component':{
            0:'atm',
            1:'atm',
            2:'atm',
            3:'atm',
            4:'atm'
        },
        'frequency':{
            0:'daily',
            1:'daily',
            2:'daily',
            3:'daily',
            4:'daily'
        },
        'experiment':{
            0:'20C',
            1:'20C',
            2:'20C',
            3:'20C',
            4:'20C'
        },
        'variable':{
            0:'FLNS',
            1:'FLNSC',
            2:'FLUT',
            3:'FSNS',
            4:'FSNSC'
        },
        'path':{
            0:'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLNS.zarr',
            1:'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLNSC.zarr',
            2:'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLUT.zarr',
            3:'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FSNS.zarr',
            4:'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FSNSC.zarr'
        }
    },
    "attributes":[
        {
            "column_name":"component",
            "vocabulary":""
        },
        {
            "column_name":"frequency",
            "vocabulary":""
        },
        {
            "column_name":"experiment",
            "vocabulary":""
        },
        {
            "column_name":"variable",
            "vocabulary":""
        }
    ],
    "assets":{
        "column_name":"path",
        "format":"zarr"
    },
    "aggregation_control":{
        "variable_column_name":"variable",
        "groupby_attrs":[
            "component",
            "experiment",
            "frequency"
        ],
        "aggregations":[
            {
                "type":"union",
                "attribute_name":"variable",
                "options":{
                    "compat":"override"
                }
            }
        ]
    }
}
```

or

**Option 2) records**: ```[{column -> value}, ... , {column -> value}]```

```yaml
{
    "esmcat_version":"0.1.0",
    "id":"aws-cesm1-le",
    "description":"This is an ESM collection for CESM1 Large Ensemble Zarr dataset publicly available on Amazon S3 (us-west-2 region)",
    "catalog_dict":[
        {
            'component':'atm',
            'frequency':'daily',
            'experiment':'20C',
            'variable':'FLNS',
            'path':'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLNS.zarr'
        },
        {
            'component':'atm',
            'frequency':'daily',
            'experiment':'20C',
            'variable':'FLNSC',
            'path':'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLNSC.zarr'
        },
        {
            'component':'atm',
            'frequency':'daily',
            'experiment':'20C',
            'variable':'FLUT',
            'path':'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FLUT.zarr'
        },
        {
            'component':'atm',
            'frequency':'daily',
            'experiment':'20C',
            'variable':'FSNS',
            'path':'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FSNS.zarr'
        },
        {
            'component':'atm',
            'frequency':'daily',
            'experiment':'20C',
            'variable':'FSNSC',
            'path':'s3://ncar-cesm-lens/atm/daily/cesmLE-20C-FSNSC.zarr'
        }
    ],
    "attributes":[
        {
            "column_name":"component",
            "vocabulary":""
        },
        {
            "column_name":"frequency",
            "vocabulary":""
        },
        {
            "column_name":"experiment",
            "vocabulary":""
        },
        {
            "column_name":"variable",
            "vocabulary":""
        }
    ],
    "assets":{
        "column_name":"path",
        "format":"zarr"
    },
    "aggregation_control":{
        "variable_column_name":"variable",
        "groupby_attrs":[
            "component",
            "experiment",
            "frequency"
        ],
        "aggregations":[
            {
                "type":"union",
                "attribute_name":"variable",
                "options":{
                    "compat":"override"
                }
            }
        ]
    }
}
```

### esm-collection-spec side

- [X] Update the [specification file](https://github.com/NCAR/esm-collection-spec/blob/master/collection-spec/collection-spec.md)
- [X] Incorporate the [`esmcol`](https://github.com/NCAR/esm-collection-spec/blob/master/esmcol_validator/validator.py) validator into `intake-esm`

### intake-esm side

- [X] Update/add a new argument `catalog_type` to [`serialize() method`](https://github.com/NCAR/intake-esm/blob/master/intake_esm/core.py#L131)???

  - Accepted values for `catalog_type` would include `dict` for `catalog_dict`     key and `file` for `catalog_file` key.
  - Errors if `catalog_type` not in `{"dict", "file"}`
  - Should we add an `orient` argument to control the type of the values of the dictionary??? For instance, `orient='dict'` would yield option 1) and `orient='records'` would yield option 2) described above.

```python
   def serialize(self, name, catalog_type='file',
                  orient='records', directory=None):
       ...
```

- [ ] Update [`_fetch_catalog()` method](https://github.com/NCAR/intake-esm/blob/master/intake_esm/core.py#L126) so that it can support reading the catalog from dictionary specified in `catalog_dict`:

```python

    @lru_cache(maxsize=None)
    def _fetch_catalog(self):
        """Get the catalog content and cache it.
        """
        if 'catalog_file' in self._col_data:
            return pd.read_csv(self._col_data['catalog_file'])
        else:
            return pd.DataFrame(self._col_data['catalog_dict'])
       ...
```

## Milestones & Timeline

| Milestone        | Deadline   | Done    |
|:-----------------|:----------:|:-------:|
| 1. Move `esmcol-validator` into its own repo | 2020-01-21 | &#9746; |
| 2. Update `esmcol-validator` and cut first release | 2020-01-21 | &#9746; |
| 3. Incorporate `esmcol-validator` into intake-esm | 2020-01-22 | &#9744; |
| 4. Support Single File Catalog in intake-esm | 2020-01-23 | &#9746; |

Pull request for #1:  [https://github.com/NCAR/esm-collection-spec/pull/14]

Pull request for #3:  [https://github.com/NCAR/intake-esm/pull/199]

Pull request for #4:  [https://github.com/NCAR/intake-esm/pull/195]

## References

- [https://github.com/NCAR/esm-collection-spec/issues/13](https://github.com/NCAR/esm-collection-spec/issues/13)

- [https://github.com/NCAR/intake-esm/pull/179#issuecomment-553630201](https://github.com/NCAR/intake-esm/pull/179#issuecomment-553630201)

- [https://github.com/NCAR/intake-esm/issues/166](https://github.com/NCAR/intake-esm/issues/166)
