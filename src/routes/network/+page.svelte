<script lang="ts">
    import "$lib/app.css";
    import Title from "$lib/title.svelte";
    let cidr = ""
    let ports = ""
    function handleSubmit() {
        cidr = cidr || "192.168.1.0/24"
        ports = ports || "502"
    }
</script>

<div class="flex flex-col items-center">
    <Title>Network</Title>
    <form class="flex flex-col" on:submit={handleSubmit}>
            <div class="flex flex-row border-2 border-black rounded-md input px-2 py-1 mb-3">
                <input type="text" class="bg-transparent focus:outline-none pr-1" bind:value={cidr} placeholder="192.168.1.0/24">
                <p>CIDR</p>
            </div>
            <div class="flex flex-row border-2 border-black rounded-md input px-2 py-1 mb-3">
                <input type="text" class="bg-transparent focus:outline-none pr-1" bind:value={ports} placeholder="502">
                <p>Ports</p>
            </div>
            <button class="border-2 border-black px-2 py-1 clickable">Scan</button>
    </form>
</div>