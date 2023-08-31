import play.core.PlayVersion
import play.sbt.PlayImport._
import sbt.Keys.libraryDependencies
import sbt._

object AppDependencies {

  private val bootstrapVersion = "7.13.0"
  

  val compile = Seq(
    ws,
    "uk.gov.hmrc"             %% "bootstrap-frontend-play-28" % bootstrapVersion
  )

  val test = Seq(
    "uk.gov.hmrc"             %% "bootstrap-test-play-28"     % bootstrapVersion            % "test",
  )
}
