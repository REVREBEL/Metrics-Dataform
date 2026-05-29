# Source Application Lookup Model

This document defines the normalized source-application model used by Metrics mapping tables.

## Naming convention

Use one standard mapping-table field name:

```text
source_application_code
```

Do not use mixed names such as `source_system`, `system`, or `source_system_category` for mapping-table joins to the source application lookup.

## Relationship path

```text
mapping_table.source_application_code
  -> metrics_core.lkp_source_application.code
  -> metrics_core.lkp_source_system_type.code
```

The granular source application identifies the actual system that produced a raw value, such as IDeaS, OPERA, SynXis, or Lighthouse. The broader source-system type identifies the application class, such as RMS, PMS, CRS, or RateShop.

## Tables

### `metrics_core.lkp_source_system_type`

Broad application type lookup.

| Column | Description |
|---|---|
| `code` | Broad type code, such as `PMS`, `CRS`, `RMS`, `RateShop`, `Marketing`, `Finance`, `Sales`, `Web`, or `Manual`. |
| `name` | Broad type display name. |
| `description` | Definition or usage notes. |
| `sort` | Display order for UI and reporting. |
| `is_active` | Active flag. |
| `insert_date` | Insert date. |
| `updated_date` | Updated date. |

### `metrics_core.lkp_source_application`

Granular source application lookup.

| Column | Description |
|---|---|
| `code` | Standard granular source application code. |
| `name` | Source application display name. |
| `short_name` | Short display name. |
| `description` | Definition or usage notes. |
| `sort` | Display order for UI and reporting. |
| `source_system_type_code` | Broad type code. Joins to `lkp_source_system_type.code`. |
| `vendor` | Application vendor or provider. |
| `is_active` | Active flag. |
| `insert_date` | Insert date. |
| `updated_date` | Updated date. |

## Mapping-table usage

The following mapping tables should use `source_application_code` as the source application foreign key:

| Mapping Table | Field | Lookup Target |
|---|---|---|
| `metrics_core.map_segment` | `source_application_code` | `metrics_core.lkp_source_application.code` |
| `metrics_core.map_source` | `source_application_code` | `metrics_core.lkp_source_application.code` |
| `metrics_core.map_rate` | `source_application_code` | `metrics_core.lkp_source_application.code` |
| `metrics_core.map_roomtype` | `source_application_code` | `metrics_core.lkp_source_application.code` |

## `map_hotel` exception

`map_hotel` should not require a source application field. Hotel/property identity mapping should resolve identifiers to `dim_property` without requiring source-system/source-application classification.

## Agent-readable spec

```yaml
source_application_model:
  standard_field_name: source_application_code
  broad_lookup_table: metrics_core.lkp_source_system_type
  granular_lookup_table: metrics_core.lkp_source_application
  relationships:
    - from: metrics_core.lkp_source_application.source_system_type_code
      to: metrics_core.lkp_source_system_type.code
      type: many_to_one
    - from: mapping_table.source_application_code
      to: metrics_core.lkp_source_application.code
      type: many_to_one
  disallowed_mapping_field_names:
    - source_system
    - system
    - source_system_category
  exception_tables:
    - table: metrics_core.map_hotel
      rule: do_not_require_source_application_code
```
