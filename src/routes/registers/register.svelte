<script lang="ts">
    import "$lib/app.css";
    import type { RegisterStore } from "$lib/register_store";
    
    export let register: RegisterStore;
</script>

<button class="group flex flex-row text-l p-2 mx-2 w-36 border-2 border-gray-600 rounded-xl items-center hover:text-white hover:border-white">
    <div class="flex flex-col text-right min-w-10">
        <div class="text-xs">{register.address}</div>
        <div class="text-xs">{register.type}</div>
    </div>
    <div class="border border-gray-600 group-hover:border-white ml-2 mr-2 min-h-8"></div>
    <div class="text-center w-full">{register.value}</div>
</button>
