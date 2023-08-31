val appName =  "excise-movement-control-system-api-tis"

lazy val microservice = Project(appName, file("."))
  .enablePlugins(play.sbt.PlayScala, SbtDistributablesPlugin)
  .settings(
    majorVersion        := 0,
    scalaVersion        := "2.13.8",
    libraryDependencies ++= AppDependencies.compile ++ AppDependencies.test,
      update / evictionWarningOptions := EvictionWarningOptions.default.withWarnScalaVersionEviction(false),
    scalacOptions += "-Wconf:src=routes/.*:s",
      scalacOptions ++= Seq(
          "-Xfatal-warnings",
          "-Wconf:src=routes/.*:silent",
          "-feature"
      )
  )
  .settings(resolvers += Resolver.jcenterRepo)
