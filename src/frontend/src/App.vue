<template>
    <div class="w-full h-screen">
        <div class="w-1/3 h-full border-r border-black">
            <div class="w-full h-full flex flex-col">
                <div class="m-10 px-3 py-2 rounded-lg font-bold text-white text-sm bg-blue-500 hover:bg-blue-600 transition-all duration-300"
                     v-on:click="createPoint"
                >
                    Создать точку
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const points = ref([])




</script>