<script lang="ts">
    import "$lib/app.css";
    import type { RegisterStore } from "$lib/register_store";
    import { SelectedRegisters } from "$lib/store";
    
    export let register: RegisterStore;

    let selected = false;

    function toggle_register() {
        const registerIndex = $SelectedRegisters.findIndex(reg => reg.address === register.address);
        if (registerIndex !== -1) {
            $SelectedRegisters.splice(registerIndex, 1);
            selected = false;
        } else {
            $SelectedRegisters.push(register);
            selected = true;
        }
    }
    $: selected = $SelectedRegisters.findIndex(reg => reg.address === register.address) !== -1;
</script>

<button draggable="true" on:click={toggle_register} class:text-white={selected} class:border-white={selected} class="group flex flex-row text-l p-2 mx-2 w-36 border-2 border-gray-600 rounded-xl items-center hover:text-white hover:border-white">
    <div class="flex flex-col text-right min-w-10">
        <div class="text-xs">{register.address}</div>
        <div class="text-xs">{register.type}</div>
    </div>
    <div class:border-white={selected} class="border border-gray-600 group-hover:border-white ml-2 mr-2 min-h-8"></div>
    <div class="text-center w-full">{register.value}</div>
</button>
