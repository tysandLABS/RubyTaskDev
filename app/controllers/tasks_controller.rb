class TasksController < ApplicationController
  def index
    @tasks = Task.order(:position)
  end

  def show
    @task = Task.find(params[:id])
  end

  def new
    @count = Task.count
    @task = Task.new(position: Task.count + 1)
    
  end

  def create
    @task = Task.new(task_params)
    if @task.save
      flash[:notice] = "Task created successfully."
      redirect_to(tasks_path)
    else
      # If save fails, redisplay the form so user can fix problems
      render('new')
    end
  end

  def edit
    @task = Task.find(params[:id])
  end

  def update
    @task = Task.find(params[:id])
    if @task.update(task_params)
      redirect_to(task_path(@task))
    else
      render('edit')
    end
  end

  def delete
    @task = Task.find(params[:id])
  end

  def destroy
    @task = Task.find(params[:id])
    @task.destroy
    redirect_to(tasks_path)
  end

  def task_params
    params.require(:task).permit(
      :name, 
      :position, 
      :completed, 
      :description
      )
  end
end
