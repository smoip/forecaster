import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput, onClick)

main =
  Html.beginnerProgram { model = model, view = view, update = update }

-- MODEL

type alias Model =
  { zipCode : String, forecast : String }

model : Model
model =
  Model "" ""

-- UPDATE

type Msg
    = UpdateZip String | GetForecast

update : Msg -> Model -> Model
update msg model =
  case msg of
    UpdateZip zipCode ->
      { model | zipCode = zipCode }
    GetForecast ->
      { model | forecast = "Forecast for: " ++ model.zipCode }

-- VIEW

view : Model -> Html Msg
view model =
  div []
    [ input [ type_ "text", placeholder "Zip Code", onInput UpdateZip ] []
    , div [] [ text model.zipCode ]
    , button [ onClick GetForecast ] [ text "Get forecast" ]
    , div [] [ text model.forecast ]
    ]
