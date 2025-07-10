# Change-Aware Data Validation with Column-Level Lineage

*Define and analyze the impact radius of data model changes*

**Author:** [Dave Flynn](https://towardsdatascience.com/author/dave-flynn/)  
**Date:** Jul 4, 2025  
**Reading time:** 8 min

![A section of Gitlab’s dbt project lineage](https://towardsdatascience.com/wp-content/uploads/2025/07/lineage-graph.jpg)
*A section of Gitlab’s dbt project lineage (Screenshot of Gitlab's publicly available dbt lineage taken by author)*

Data transformation tools like dbt make constructing SQL data pipelines easy and systematic. But even with the added structure and clearly defined data models, pipelines can still become complex, which makes debugging issues and validating changes to data models difficult.

The increasing complexity of data transformation logic gives rise to the following issues:

1. **Traditional code review processes** only look at *code* changes and exclude the data impact of those changes.
2. **Data impact resulting from code changes is hard to trace**. In sprawling DAGs with nested dependencies, discovering how and where data impact occurs is extremely time-consuming, or near impossible.

Gitlab’s [dbt DAG](https://dbt.gitlabdata.com/#!/overview?g_v=1) (shown in the featured image above) is the perfect example of a data project that's already a house-of-cards. Imagine trying to follow a simple SQL logic change to a column through this entire lineage DAG. Reviewing a data model update would be a daunting task.

How would you approach this type of review?

## What is data validation?

Data validation refers to the process used to determine that the data is correct in terms of real-world requirements. This means ensuring that the **SQL logic** in a data model behaves as intended by verifying that the data is correct. Validation is usually performed after modifying a data model, such as accommodating new requirements, or as part of a refactor.

### A unique review challenge

Data has states and is directly affected by the transformation used to generate it. This is why reviewing data model changes is a unique challenge, because both the code *and* the data needs to be reviewed.

Due to this, data model updates should be reviewed not only for completeness, but also context. In other words, that the data is correct and existing data and metrics were not unintentionally altered.

### Two extremes of data validation

In most data teams, the person making the change relies on institutional knowledge, intuition, or past experience to assess the impact and validate the change.

> *“I’ve made a change to X, I think I know what the impact should be. I’ll check it by running Y”*

The validation method usually falls into one of two extremes, neither of which is ideal:

1. **Spot-checking** with queries and some high-level checks like row count and schema. It’s fast but risks missing actual impact. Critical and silent errors can go unnoticed.
2. **Exhaustive checking** of every single downstream model. It’s slow and resource intensive, and can be costly as the pipeline grows.

This results in a data review process that is unstructured, hard to repeat, and often introduces silent errors. A new method is required that helps the engineer to perform precise and targeted data validation.

## A better approach through understanding data model dependencies

To validate a change to a data project, it’s important to understand the relationship between models and how data flows through the project. These dependencies between models inform us how data is passed and transformed from one model to another.

### Analyze the relationship between models

As we’ve seen, data project DAGs can be huge, but a data model change only affects a subset of models. By isolating this subset and then analyzing the relationship between the models, you can peel back the layers of complexity and focus just on the models that actually need validating, given a specific SQL logic change.

The types of dependencies in a data project are:

**Model-to model**

A structural dependency in which columns are selected from an upstream model.

```sql
--- downstream_model
select
  a,
  b
from {{ ref("upstream_model") }}
```

**Column-to-column**

A projection dependency that selects, renames, or transforms an upstream column.

```sql
--- downstream_model
select
  a,
  b as b2
from {{ ref("upstream_model") }}
```

**Model-to-column**

A filter dependency in which a downstream model uses an upstream model in a where, join, or other conditional clause.

```sql
-- downstream_model
select
  a
from {{ ref("upstream_model") }}
where b > 0
```

Understanding the dependencies between models helps us to define the impact radius of a data model logic change.

## Identify the impact radius

When making changes to a data model’s SQL, it’s important to understand which other models might be affected (the models you must check). At the high level, this is done by model-to-model relationships. This subset of DAG nodes is known as the impact radius.

In the DAG below, the impact radius includes nodes B (the modified model) and D (the downstream model). In dbt, these models can be identified using the modified+ selector.

![DAG showing modified model B and downstream dependency D. Upstream model A and unrelated model C are not impacted.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/lineage-1.png)
*DAG showing modified model B and downstream dependency D. Upstream model A and unrelated model C are not impacted (Image by author)*

Identifying modified nodes and downstream is a great start, and by isolating changes like this you will reduce the potential data validation area. However, this could still result in a large number of downstream models.

Classifying the *types* of SQL changes can further help you to prioritize which models actually require validation by understanding the severity of the change, eliminating branches with changes that are known to be safe.

## Classify the SQL change

Not all SQL changes carry the same level of risk to downstream data, and so should be categorized accordingly. By classifying SQL changes this way, you can add a systematic approach to your data review process.

A SQL change to a data model can be classified as one of the following:

### Non-breaking change

Changes that do not impact the data in downstream models such as adding new columns, adjustments to SQL formatting, or adding comments etc.

```sql
-- Non-breaking change: New column added
select
  id,
  category,
  created_at,
  -- new column
  now() as ingestion_time
from {{ ref('a') }}
```

### Partial-breaking change

Changes that only impact downstream models that reference certain columns such as removing or renaming a column; or modifying a column definition.

```sql
-- Partial breaking change: `category` column renamed
select
  id,
  created_at,
  category as event_category
from {{ ref('a') }}
```

### Breaking change

Changes that impact all downstream models such as filtering, sorting, or otherwise changing the structure or meaning of the transformed data.

```sql
-- Breaking change: Filtered to exclude data
select
  id,
  category,
  created_at
from {{ ref('a') }}
where category != 'internal'
```

## Apply classification to reduce scope

After applying these classifications the impact radius, and the number of models that need to be validated, can be significantly reduced.

![DAG showing three categories of change: non-breaking, partial-breaking, and breaking](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/lineage-2.png)
*DAG showing three categories of change: non-breaking, partial-breaking, and breaking (Image by author)*

In the above DAG, nodes B, C and F have been modified, resulting in potentially 7 nodes that need to be validated (C to E). However, not each branch contains SQL changes that actually require validation. Let’s take a look at each branch:

#### Node C: Non-breaking change

C is classified as a non-breaking change. Therefore both C and H do not need to be checked, they can be eliminated.

#### Node B: Partial-breaking change

B is classified as a partial-breaking change due to change to the column B.C1. Therefore, D and E need to be checked *only* if they reference column B.C1.

#### Node F: Breaking change

The modification to model F is classified as a breaking-change. Therefore, all downstream nodes (G and E) need to be checked for impact. For instance, model g might aggregate data from the modified upstream column

The initial 7 nodes have already been reduced to 5 that need to be checked for data impact (B, D, E, F, G). Now, by inspecting the SQL changes at the column level, we can reduce that number even further.

## Narrowing the scope further with column-level lineage

Breaking and non-breaking changes are easy to classify but, when it comes to inspecting partial-breaking changes, the models need to be analyzed at the column level.

Let’s take a closer look at the partial-breaking change in model B, in which the logic of column c1 has been modified. This modification could potentially result in 4 impacted downstream nodes: D, E, K, and J. After tracking column usage downstream, this subset can be further reduced.

![DAG showing the column-level lineage used to trace the downstream impact of a change to column B.c1](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/lineage-3.png)
*DAG showing the column-level lineage used to trace the downstream impact of a change to column B.c1 (Image by author)*

Following column B.c1 downstream we can see that:

- B.c1 → D.c1 is a column-to-column (projection) dependency.
- D.c1 → E is a model-to-column dependency.
- D → K is a model-to-model dependency. However, as D.c1 is not used in K, this model can be eliminated.

Therefore, the models that need to be validated in this branch are B, D, and E. Together with the breaking change F and downstream G, the total models to be validated in this diagram are F, G, B, D, and E, or just 5 out of a total of 9 potentially impacted models.

## Conclusion

Data validation after a model change is difficult, especially in large and complex DAGs. It’s easy to miss silent errors and performing validation becomes a daunting task, with data models often feeling like black boxes when it comes to downstream impact.

### A structured and repeatable process

By using this change-aware data validation technique, you can bring structure and precision to the review process, making it systematic and repeatable. This reduces the number of models that need to be checked, simplifies the review process, and lowers costs by only validating models that actually require it.

## Before you go…

Dave is a senior technical advocate at [Recce](https://reccehq.com), where we’re building a toolkit to enable advanced data validation workflows. He’s always happy to chat about SQL, data engineering, or helping teams navigate their data validation challenges. Connect with Dave on [LinkedIn](https://www.linkedin.com/in/daveflynn81/).

Research for this article was made possible by my colleague Chen En Lu ([Popcorny](https://github.com/popcornylu)). 