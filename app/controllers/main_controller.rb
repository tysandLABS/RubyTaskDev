class MainController < ApplicationController
  def index
    render("index")
  end

  def about
    @created_by = "Tyrone"
    @id = params['id']
    @page = params[:page]
  end

  def hello
    redirect_to(action: "index")
  end
end
