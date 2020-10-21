<template>
<v-app>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px" >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#4c4c65"
          dark
          v-bind="attrs"
          v-on="on"
          class="align-center"
        >
          업무정보
        </v-btn>
      </template>
      <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
        <v-card-title class="pt-7 d-flex justify-center">
          <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">업무 정보</span>
        </v-card-title>
        <v-card-text>
           <v-container fluid>


    <v-row style="height:70px;">
      <v-col cols="4" >
        <v-subheader class="workform">업무명</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          color="#4c4c65"
          v-model="workname"
          solo
          label="업무명"
          clearable
        >
        </v-text-field>
      </v-col>
    </v-row>

    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">담당자</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          color="#4c4c65"
          v-model="workman"
          solo
          label="담당자"
          clearable
        >
        </v-text-field>
      </v-col>
    </v-row>
  

    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">마감 시간</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          v-model="worktime"
          solo
          type="time"
          color="#4c4c65"
        ></v-text-field>
      </v-col>
    </v-row>
    
     <v-row style="height:160px;">
      <v-col cols="4">
        <v-subheader class="workform">상세 업무</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          color="#4c4c65"
          v-model="worklist"
          solo
          label="상세 업무"
          clearable
          height="150"
        >
        </v-text-field>
      </v-col>

    </v-row>
     <v-row style="height:20px;">
      <v-col cols="4">
        <v-subheader class="workform">완료 여부</v-subheader>
      </v-col>
      <v-col cols="5">
      </v-col>
      <v-col cols="3">
        <v-select
        color ="#4c4c65"
      v-model="select"
      :items="workcomplete"
      solo
      max-width ="1"
    ></v-select>
      </v-col>
    </v-row>

  </v-container>
      
        </v-card-text>
        <v-card-actions class="pa-7 d-flex justify-center">
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-btn x-large color="#4c4c65" class="white--text" @click="dialog = false">확인</v-btn>
          <v-spacer></v-spacer>
          <v-btn x-large color="#FFFFFF" class="black--text" @click="dialog = false">취소</v-btn>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</v-app>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      workname : '업무1',
      workman : '김기훈',
      worktime : '12:20:00',
      worklist : '-xx하기',
      select : '미완료',
      workcomplete: [
        '완료',
        '미완료'
      ],
    }),
  }
</script>
<style scoped>
  .workform {
    font-weight : bold;
    font-size: 1.2em;
   
  }
</style>