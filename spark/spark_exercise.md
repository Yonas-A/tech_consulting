### Spark

#### Beginner Level

1. What is Apache Spark, and why is it faster than Hadoop MapReduce?

    - spark is a distributed data processing engine.

    - Spark uses in memory processing while MapReduce uses disk processing

2. Name two common use cases for Spark in real-world applications.
    - real time data streaming in a finance

3. What are the main components of the Spark ecosystem?
    1. Driver
    2. Cluster Manager
    3. Executor

4. What is the difference between RDDs and DataFrames?

    - RDDs: Immutable distributed collection of objects

    - DataFrames: distributed collection of data organized into named columns, similar to a table in a relational database or a pandas DataFrame

5. Explain the concept of lazy evaluation in Spark.
    - in lazy evaluation, transformations are recorded in a logical plan(DAG) and are executed **only** when an action is triggered.

6. What triggers Spark to actually execute transformations?
    - actions

7. In Spark architecture, what is the role of the Driver and Executors?
    - Driver: creates a plan of execution, SparkSession, converts transformations into a DAG execution plan

    - Executors: worker processes that perform actual data processing including executing tasks, storing data for caching, parallel processing, returing result

8. What is Spark SQL, and why would you use it?
    - Spark SQL is a module in Apache Spark for structured data processing.

    - You can write SQL queries directly on DataFrames using spark.sql()

---

#### Intermediate Level

1. Explain the difference between narrow and wide transformations with examples.

    - `narrow transformation`: each partition of child RDD only depends on only one partition of the parent RDD. No data suffling across cluster is required. `one-to-one` partition

        ```py
        df1 = df.filter("age > 30")
        # map(), union(), mapPartitions()
        ```

    - `wide transformation`: when multiple parent partitions RDD contribute to a single child partition RDD, requring data shuffling across the cluster. `many-to-many` partion

        ```py
        df2 = df.groupBy("department").count()
        # groupByKey(), reduceByKey(), join(), distinct()
        ```

2. What is a Spark DAG, and how does it optimize execution?

    - ***DAG*** is a Directed Acyclic Graph, a logical execution plan that represents the sequence of transformations applied to the data before execution

    - Spark’s DAG optimizes execution by

        - delaying execution (lazy evaluation)
        - grouping transformations into stages
        - pipelining narrow transformations
        - minimizing shuffles
        - choosing optimal join strategies
        - adapting at runtime with AQE.

3. Compare Spark deployment modes: Local, YARN, Standalone, and Kubernetes.
    - local

4. When would you use broadcast joins in Spark?

    - broadcast join is used when one of the datasets is small enough to fit in memory on each executor. Spark sends (broadcasts) the small dataset to all worker nodes so the join can happen locally without shuffling the large dataset across the cluster.

    - when avoiding expensive shuffle

    - on star schema architecture (large fact table over smaller dimension)

5. What are the advantages of using Parquet or ORC over CSV in Spark?

    - both `parquet` and `ORC` use columnar storage while csv stores data row wise

    - much better compression

    - built-in schema inforcer with `parquet` and `ORC`

6. What is the Catalyst Optimizer, and why is it important?

    - its a query optimization framework that analyzes and transforms logical query plans into efficient physical execution plans. It enabling Spark to execute SQL queries and DataFrame operations at large scale with high performance and reliability

    - it enables automatic performace optimization

    - Faster query execution

    - Efficient resource usage
        - disk I/O
        - network shuffles
        - CPU overhead
        - memory usage

7. Explain the difference between repartition() and coalesce().

    - `repartition`
        - increases/decreases partition.
        - always performs full shuffles data
        - Distributes data evenly across all partitions.
        - Useful when you need balanced partitions for parallelism.

    - `colesce`
        - reduces partition without a full shuffle if possible
        - Data distribution may be uneven if no shuffle

8. Why is Spark fault-tolerant?
    - Spark uses lineage (DAG history). So if a partition is lost, Spark recomputes it using previous transformations.

---

#### Advanced Level

1. How does Spark handle stage division in jobs, and how do wide transformations affect this?

    - Spark divides a job into stages at shuffle boundaries. Within a stage, tasks can run independently and in parallel

    - In wide transformations, each parent RDD may affect multiple child RDD, requring shuffle. These shuffle mark `stage boundary`, which trigger a new stage

    - **Rules for Stage Division**

        - Stages change at wide transformations (shuffle).

        - Narrow transformations can be pipelined into a single stage.

        - Multiple stages can exist in a job, depending on the number of shuffle boundaries.

2. Explain the differences between RDD, DataFrame, and Dataset APIs.

    1. **RDD** (Resilient Distributed Dataset)

        - Core abstraction of Spark.
        - Low-level API for distributed data.
        - No schema — Spark treats each element as an object.
        - Operations: transformations (map, filter, reduceByKey) and actions (collect, count).
        - Performance: Slower because no query optimization
        - Object serialization overhead

    2. **DataFrame**

        - Higher-level abstraction over RDDs.
        - Schema-based, like a SQL table (columns + types).
        - Optimized using Catalyst and Tungsten.
        - Supports SQL queries and API operations like select, filter, groupBy.

    3. **Dataset**

        - Strongly-typed, distributed collection of JVM objects.
        - Combines RDD type safety with DataFrame optimizations.
        - Only available in Scala/Java (Python does not have Dataset; PySpark DataFrame is equivalent to untyped Dataset).

3. What is vectorized query execution in Spark, and when is it beneficial?

    - **Vectorized execution** is a technique where Spark processes batches of rows (columnar batches) at a time, rather than one row at a time.

    - its benificial on
        - when working with columnar Data (Parquet or ORC)

        - Analytical Queries

        - Large data volumes: vectorization reduces CPU time significantly

        - CPU-bound Operations: Operations that spend a lot of time in arithmetic, comparisons, or filtering rather than waiting for I/O

4. Discuss strategies to deal with data skew in Spark joins.

    - **Data skew** occurs when the data is unevenly distributed across partitions, causing some partitions to be much larger than others. This leads to unequal workloads and can slow down or even crash your Spark job.
    ` `
    - Repartition/Coalesce Carefully

    - use broadcast join to send the small table to all nodes

    - Use skewed join optimization ( built in optimization, Spark 3.0+)

5. How do Spark Window functions differ from groupBy aggregations?

    - In Window function
        - original rows are preserved
        - aggregates data but a new column is added
        - ordering is supported

    - GroupBy
        - compresses rows to a single summary per group
        - aggregates data
        - ordering is not considered

6. What role do Tungsten and Catalyst play in Spark performance tuning?

    - Catalyst optimizer is a logical/physical query optimization that generates efficient execution plans, improving performance and resource utilization.

    - Tungsten engine works taking this efficient execution plan and executes it efficiently at runtime with CPU and memory optimizations.

        ```cs
        Catalyst -> the smart planner 
        Tungsten -> the high-performance executor
        ```

7. When would you choose Spark Structured Streaming over Spark Streaming?

    - Structured Streaming
        - Unified batch + streaming code.

        - High-level declarative APIs.

        - Event-time processing and late data handling.

        - Exactly-once semantics.

        - Easier integration with modern data sinks.

    - Spark Streaming
        - if you have an existing DStream-based pipeline
        - need very low-latency micro-batching where full Structured Streaming is overkill

8. How do you tune partition sizes in Spark for optimal performance?

    - Adjust based on cluster size and data volume:
    - Consider Skewed Data
