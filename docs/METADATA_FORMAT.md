# Metadata Format Documentation

Complete specification for the JSON and YAML metadata formats used in the awesome-claude-skills metadata management system.

## Table of Contents
1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Resource Schema](#resource-schema)
4. [User Metadata Schema](#user-metadata-schema)
5. [Data Types](#data-types)
6. [Validation Rules](#validation-rules)
7. [Examples](#examples)
8. [Best Practices](#best-practices)

## Overview

This project uses two metadata file formats:
- **JSON** - Machine-readable, ideal for API consumption
- **YAML** - Human-readable, easier to edit manually

Both formats contain identical data, just different serialization.

### Why Two Formats?

- **JSON**: Perfect for server responses, JavaScript applications, and automated processing
- **YAML**: Better for human editing, version control diffs, and documentation

## File Structure

### Australian Resources Files

Two files contain the same data:
- `/metadata/australian-resources.json`
- `/metadata/australian-resources.yaml`

Both contain:
- Array of resource objects
- Metadata object with file information

### User Metadata File

- `/metadata/user-metadata.json`

Contains user profile and contribution information.

## Resource Schema

Each resource in the Australian resources collection follows this schema:

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✅ Yes | Unique identifier for the resource |
| `title` | string | ✅ Yes | Full official title of the resource |
| `alternateTitle` | string | ✅ Yes | Short name or acronym |
| `organization` | string | ✅ Yes | Organization providing/maintaining the resource |
| `type` | string | ✅ Yes | Type/category of resource |
| `description` | string | ✅ Yes | Detailed description of the resource |
| `subjects` | array | ✅ Yes | Array of subject area strings |
| `accessType` | string | ✅ Yes | Access level (e.g., "Open Access", "Subscription") |
| `url` | string | ✅ Yes | Official URL for the resource |
| `dateAdded` | string | ✅ Yes | Date added in ISO 8601 format (YYYY-MM-DD) |
| `addedBy` | string | ✅ Yes | Username of person who added resource |

### Field Descriptions

#### id
- **Format**: `{prefix}-{number}` (e.g., `abs-002`)
- **Pattern**: Lowercase letters and numbers, hyphen-separated
- **Uniqueness**: Must be unique across all resources
- **Examples**: `aidh-001`, `austlii-005`, `ada-008`

#### title
- **Format**: Free text, title case
- **Length**: Typically 3-80 characters
- **Style**: Official full name as used by organization
- **Examples**:
  - "Australian Bureau of Statistics"
  - "Australasian Legal Information Institute"

#### alternateTitle
- **Format**: Free text, typically uppercase acronym
- **Length**: 2-30 characters
- **Purpose**: Short, recognizable name
- **Examples**: "ABS", "AIDH", "AustLII"

#### organization
- **Format**: Free text, official organization name
- **Length**: 10-100 characters
- **Examples**:
  - "Australian Government"
  - "University of Technology Sydney and University of New South Wales"

#### type
- **Format**: Categorical string
- **Common values**:
  - `Database`
  - `Statistics`
  - `Research Database`
  - `News Database`
  - `Legal Database`
  - `Data Archive`
  - `Policy Database`
  - `Collection`
  - `Repository`

#### description
- **Format**: Free text, sentence case
- **Length**: 50-500 characters
- **Style**: One or two sentences describing purpose and scope
- **Should include**:
  - What the resource is
  - What it provides
  - Who it serves

#### subjects
- **Format**: Array of strings
- **Length**: 2-10 items per resource
- **Style**: Title Case, specific topics
- **Examples**:
  ```json
  ["Statistics", "Demographics", "Economics"]
  ["Law", "Legal Research", "Legislation"]
  ```

#### accessType
- **Format**: Categorical string
- **Common values**:
  - `Open Access` - Free, public access
  - `Subscription` - Paid or institutional access
  - `Registration Required` - Free but requires account
  - `Limited Access` - Restricted to specific users

#### url
- **Format**: Valid HTTP/HTTPS URL
- **Must**: Be the official, canonical URL
- **Should**: Point to the main landing page, not subpages
- **Examples**:
  - `https://www.abs.gov.au`
  - `https://www.austlii.edu.au`

#### dateAdded
- **Format**: ISO 8601 date string: `YYYY-MM-DD`
- **Examples**: `2026-01-15`, `2025-12-31`
- **Timezone**: Dates are recorded in UTC

#### addedBy
- **Format**: Username string
- **Examples**: `wsx7524999`, `johndoe`
- **Should match**: Username in user-metadata.json

## User Metadata Schema

The user metadata file (`user-metadata.json`) has a different schema:

### Top-Level Structure

```json
{
  "user": { ... },
  "metadata": { ... }
}
```

### User Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `username` | string | ✅ Yes | Unique username |
| `profile` | object | ✅ Yes | User profile information |
| `qualifications` | array | ✅ Yes | List of qualifications/skills |
| `contributions` | object | ✅ Yes | Contribution statistics |
| `preferences` | object | ❌ No | User preferences |

#### profile Object

```json
{
  "role": "string",
  "focus": "string",
  "institution": "string"
}
```

#### contributions Object

```json
{
  "resourcesAdded": number,
  "lastContribution": "YYYY-MM-DD",
  "specializations": ["string"]
}
```

#### preferences Object

```json
{
  "metadataFormat": "JSON|YAML",
  "documentationStyle": "string",
  "platform": "string"
}
```

## Data Types

### String
- UTF-8 encoded text
- No maximum length (but see field-specific guidelines)
- Can include Unicode characters

### Array
- Ordered list of values
- Typically contains strings
- Minimum 1 item (unless optional)

### Number
- Integer or decimal
- Used for counts and statistics

### Date String
- ISO 8601 format: `YYYY-MM-DD`
- Example: `2026-01-15`

### URL String
- Valid HTTP or HTTPS URL
- Must be accessible
- Should use HTTPS when available

## Validation Rules

### Required Fields
All required fields must be present. Missing required fields will cause validation errors.

### Unique IDs
Resource IDs must be unique within the resources array.

### Valid URLs
URLs must:
- Start with `http://` or `https://`
- Be properly formatted
- Not contain spaces

### Date Format
Dates must:
- Match pattern: `YYYY-MM-DD`
- Use valid months (01-12)
- Use valid days for the month

### Non-Empty Arrays
Arrays marked as required must contain at least one element.

### Non-Empty Strings
Required string fields cannot be empty or whitespace-only.

## Examples

### Complete Resource Example (JSON)

```json
{
  "id": "abs-002",
  "title": "Australian Bureau of Statistics",
  "alternateTitle": "ABS",
  "organization": "Australian Government",
  "type": "Statistics",
  "description": "National statistical agency providing comprehensive data and analysis on Australia's economy, population, environment, and social conditions. Primary source for official Australian statistics.",
  "subjects": [
    "Statistics",
    "Demographics",
    "Economics",
    "Census Data",
    "Government Data"
  ],
  "accessType": "Open Access",
  "url": "https://www.abs.gov.au",
  "dateAdded": "2026-01-15",
  "addedBy": "wsx7524999"
}
```

### Complete Resource Example (YAML)

```yaml
- id: abs-002
  title: Australian Bureau of Statistics
  alternateTitle: ABS
  organization: Australian Government
  type: Statistics
  description: >-
    National statistical agency providing comprehensive data and analysis on
    Australia's economy, population, environment, and social conditions. Primary
    source for official Australian statistics.
  subjects:
    - Statistics
    - Demographics
    - Economics
    - Census Data
    - Government Data
  accessType: Open Access
  url: https://www.abs.gov.au
  dateAdded: '2026-01-15'
  addedBy: wsx7524999
```

### User Metadata Example

```json
{
  "user": {
    "username": "wsx7524999",
    "profile": {
      "role": "Repository Maintainer",
      "focus": "Academic Resources Management",
      "institution": "Research Community"
    },
    "qualifications": [
      "Information Management",
      "Research Data Curation",
      "Academic Resource Discovery"
    ],
    "contributions": {
      "resourcesAdded": 8,
      "lastContribution": "2026-01-15",
      "specializations": [
        "Australian Academic Resources",
        "Research Data Management",
        "Library Sciences"
      ]
    },
    "preferences": {
      "metadataFormat": "JSON",
      "documentationStyle": "Comprehensive",
      "platform": "iOS/iSH"
    }
  },
  "metadata": {
    "created": "2026-01-15",
    "version": "1.0",
    "lastUpdated": "2026-01-15"
  }
}
```

## Best Practices

### 1. Consistency

**DO:**
- Use consistent casing (Title Case for titles, sentence case for descriptions)
- Follow the same pattern for all IDs
- Use standard terminology

**DON'T:**
- Mix casing styles
- Use inconsistent ID formats
- Use non-standard abbreviations without explanation

### 2. Completeness

**DO:**
- Fill all required fields
- Provide comprehensive descriptions
- Include all relevant subject areas
- Use official URLs

**DON'T:**
- Leave fields empty
- Use vague descriptions
- Omit important subjects
- Use shortened URLs

### 3. Accuracy

**DO:**
- Verify URLs are correct and working
- Use official organization names
- Check dates are in correct format
- Validate data before committing

**DON'T:**
- Guess at information
- Use outdated URLs
- Fabricate data
- Skip verification

### 4. Maintainability

**DO:**
- Use descriptive IDs
- Keep descriptions concise but informative
- Update dates when modifying records
- Document changes in commit messages

**DON'T:**
- Use cryptic IDs
- Write overly long descriptions
- Forget to update metadata
- Make undocumented changes

### 5. JSON vs YAML

**Use JSON when:**
- Serving via API
- Processing programmatically
- Need strict validation
- Performance is critical

**Use YAML when:**
- Editing manually
- Reviewing changes in git diffs
- Documentation
- Human readability is priority

### 6. Adding New Resources

When adding a new resource:

1. Choose a unique ID following the pattern
2. Use the official resource name
3. Write a clear, comprehensive description
4. Add relevant subject tags
5. Verify the URL works
6. Set accessType accurately
7. Use current date for dateAdded
8. Include your username in addedBy
9. Validate JSON/YAML syntax
10. Update both JSON and YAML files

### 7. Version Control

```bash
# Before editing
git pull origin main

# After editing
git add metadata/
git commit -m "Add [Resource Name] to metadata"
git push origin main
```

### 8. Validation

Before committing, validate your JSON:

```bash
# Using Python
python3 -m json.tool metadata/australian-resources.json

# Using jq
jq '.' metadata/australian-resources.json

# Using Node.js
node -e "console.log(JSON.stringify(require('./metadata/australian-resources.json'), null, 2))"
```

For YAML:

```bash
# Using Python
python3 -c "import yaml; yaml.safe_load(open('metadata/australian-resources.yaml'))"
```

## Schema Versioning

The metadata format follows semantic versioning:

- **Major version** (1.x.x): Breaking changes to schema
- **Minor version** (x.1.x): New fields added (backward compatible)
- **Patch version** (x.x.1): Documentation updates, no schema changes

Current version: **1.0**

## Future Extensions

Potential future additions to the schema:

- `language` - Resource language(s)
- `geographicCoverage` - Geographic scope
- `temporalCoverage` - Time period covered
- `license` - Usage license
- `relatedResources` - Links to related resources
- `contactEmail` - Support contact
- `apiEndpoint` - If resource has an API
- `lastVerified` - Last verification date
- `status` - Active, archived, etc.

## Resources

### Validation Tools
- [JSONLint](https://jsonlint.com/) - JSON validator
- [YAML Lint](http://www.yamllint.com/) - YAML validator
- [JSON Schema Validator](https://www.jsonschemavalidator.net/)

### Documentation
- [JSON Specification](https://www.json.org/)
- [YAML Specification](https://yaml.org/spec/)
- [ISO 8601 Date Format](https://en.wikipedia.org/wiki/ISO_8601)

---

**Last Updated:** 2026-01-15  
**Version:** 1.0  
**Schema Version:** 1.0
