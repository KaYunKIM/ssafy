<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col form-inline">
        <b-form-input 
          v-model="newTask" 
          placeholder="Enter Task" 
          @keyup.enter="add"
        >
        </b-form-input>
        <b-button class="ml-2"
          variant="primary"
          @click="add"
        >Add
        </b-button>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3">
        <div class="p-2 alert alert-secondary">
          <h3>BackLog</h3>
          <!-- <draggable/> -->
          <draggable class="list-group kanban-column" :list="Backlog" group="tasks">
            <div class="list-group-item" v-for="task in Backlog" :key="task.name">
              {{ task.name }}
            </div>
          </draggable>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-2 alert alert-primary">
          <h3>InProgress</h3>
          <!-- <draggable/> -->
          <draggable class="list-group kanban-column" :list="InProgress" group="tasks">
            <div class="list-group-item" v-for="task in InProgress" :key="task.name">
              {{ task.name }}
            </div>
          </draggable>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-2 alert alert-warning">
          <h3>Done</h3>
          <!-- <draggable/> -->
          <draggable class="list-group" :list="Done" group="tasks">
            <div class="list-group-item" v-for="task in Done" :key="task.name">
              {{ task.name }}
            </div>
          </draggable>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable"

export default {
  name: 'App',
  components: {
    draggable
  },
  data() {
    return {
      newTask: "",
      Backlog: [
        {name: "Code SignUpPage"},
        {name: "Test Dashboard"},
        {name: "Style Registration"},
        {name: "Help with Designs"},
      ],
      InProgress: [],
      Tested: [],
      Done: [],
    }
  },
  // To add New Tasks
  methods: {  
    add() {
      if(this.newTask) {
        this.Backlog.push({name: this.newTask})
        this.newTask = ""
      }
    }
  }
}
</script>

<style>
.kanban-column {
  min-height: 300px;
}
</style>
